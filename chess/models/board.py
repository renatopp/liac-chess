# =============================================================================
# Federal University of Rio Grande do Sul (UFRGS)
# Connectionist Artificial Intelligence Laboratory (LIAC)
# Renato de Pontes Pereira - rppereira@inf.ufrgs.br
# =============================================================================
# Copyright (c) 2011 Renato de Pontes Pereira, renato.ppontes at gmail dot com
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in 
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# =============================================================================

import chess
from .pieces import *

__all__ = ['Board']

PIECES = {
    'p': Pawn,
    'r': Rook,
    'b': Bishop,
    'q': Queen,
    'n': Knight,
    # 'k': King, # no king for now
}

class Board(object):
    '''Board class is the structure responsible to store the game pieces, and 
    to handle the game rules and the game flow. 

    The board cells are represented here in the form of a matrix (a list of 
    lists, precisely).
    '''

    def __init__(self, board='.'*64, win_methods=[], tie_methods=[], 
                 allow_enpassant=False, allow_castle=False, 
                 allow_rook_promotion=False, allow_queen_promotion=False,
                 allow_knight_promotion=False, allow_bishop_promotion=False):
        '''Board constructor.

        The `board` parameter is a string defining the initial position of 
        pieces in this board. It must be a 64-characters string where the 
        character ``.`` represents an empty cell and the characters ``prbqnk``
        represent the chess pieces. In this notation, the lowercase characters 
        represent the black pieces, and the uppercase characters represent the 
        white pieces. The first position of the string represents the ``A8``
        cell of the chess board, the second position of the string is the 
        ``A7`` cell, and so on.

        The ``win_methods`` parameter is a list containing function that,
        receiving a ``Board`` object, verify if one player has won the game 
        , returning ``chess.BLACK`` or ``chess.WHITE``, or returning 
        ``chess.NONE``if no winning condition has been reached.

        Similarly, ``tie_methods`` is a list containing function that,
        receiving a ``Board`` object, verify if the game ended in a draw. 
        These functions return a boolean.

        Both ``win_methods`` and ``tie_methods``, actually are a list with the
        function names. When the board is initialized, this class search the 
        functions in the ``chess.models`` namespace to use them.

        All other parameter are flags that turn on or off some game rules, such
        as the enpassant and castle movement or the pawn promotions.

        :param board: a string with the initial board configuration. Default to
                      empty board.
        :param win_methods: a list with functions that verify the end-game 
                            conditions. Default to empty list.
        :param tie_methods: a list with function that verify the tie 
                            conditions. Default to empty list.
        :param allow_enpassant: is enpassant movement allowed in this game? 
                                Default to false.
        :param allow_castle: is castle movement allowed in this game? Default 
                             to false.
        :param allow_rook_promotion: is promotion to rook allowed in this game?
                                     Default to false.
        :param allow_queen_promotion: is promotion to queen allowed in this
                                      game? Default to false.
        :param allow_knight_promotion: is promotion to knight allowed in this 
                                       game? Default to false.
        :param allow_bishop_promotion: is promotion to bishop allowed in this 
                                       game? Default to false.
        '''

        # End game verifiers
        self.win_methods = self._get_win_methods(win_methods)
        self.tie_methods = self._get_tie_methods(tie_methods)

        # Game rule flags
        self.allow_enpassant = allow_enpassant
        self.allow_castle = allow_castle
        self.allow_rook_promotion = allow_rook_promotion
        self.allow_queen_promotion = allow_queen_promotion
        self.allow_knight_promotion = allow_knight_promotion
        self.allow_bishop_promotion = allow_bishop_promotion

        # Board structures
        self._cells = [[None for j in xrange(8)] for i in xrange(8)]
        self.pieces = []
        self.black_pieces = []
        self.white_pieces = []

        # State variables
        # - Enpassant
        self.enpassant = None
        self.enpassant_piece = None

        # - Castle
        self.white_has_queen_castle = False
        self.white_has_king_castle = False
        self.black_has_queen_castle = False
        self.black_has_king_castle = False

        # - Check
        self.black_in_check = False
        self.white_in_check = False

        # - Other state variables
        self.who_moves = chess.WHITE
        self.nocapture_moves = 0
        self.bad_move = False
        self.white_infractions = 0
        self.black_infractions = 0
        self.move_time = chess.config['max_move_time']
        self.game_time = 0
        self.white_time = 0
        self.black_time = 0
        self.winner = chess.NONE
        self.draw = False

        # Initializes the board
        self.set_board(board)

    def _get_win_methods(self, methods):
        '''Receive a list of function names and returns a list of function 
        objects. The functions must be in the ``chess.models`` namespace, 
        otherwise a `ValueError` will be raised.

        :param methods: a list of function names.
        :return: a list of functions.
        '''
        r = []

        for method_name in methods:
            name = 'win_'+method_name
            if hasattr(chess.models, name):
                r.append(getattr(chess.models, name))
            else:
                raise ValueError('Win method "%s" not found.'%method_name)

        return r

    def _get_tie_methods(self, methods):
        '''Receive a list of function names and returns a list of function 
        objects. The functions must be in the ``chess.models`` namespace, 
        otherwise a `ValueError` will be raised.

        :param methods: a list of function names.
        :return: a list of functions.
        '''
        r = []

        for method_name in methods:
            name = 'tie_'+method_name
            if hasattr(chess.models, name):
                r.append(getattr(chess.models, name))
            else:
                raise ValueError('Tie method "%s" not found.'%method_name)

        return r

    def _verify_win(self):
        '''Verify all the win conditions by calling the functions in the 
        `win_methods` list. The result is recorded in the `winner` variable.
        '''

        for win in self.win_methods:
            r = win(self)
            if r != chess.NONE:
                self.winner = r
                return

    def _verify_tie(self):
        '''Verify all the draw conditions by calling the functions in the 
        `tie_methods` list. The result is recorded in the `draw` variable.
        '''

        for tie in self.tie_methods:
            if tie(self):
                self.draw = True
                return

    def __getitem__(self, pos):
        '''Access the board cells

        :param pos: a 2-tuple with the board row and col.
        :return: the piece localized in the position or None.
        '''
        if not 0 <= pos[0] <= 7 or not 0 <= pos[1] <= 7:
            return None

        return self._cells[pos[0]][pos[1]]

    def __setitem__(self, pos, value):
        '''Set the piece at a given positions in the board.

        :param pos: a 2-tuple with the board row and col.
        :param value: a piece or None.
        '''

        self._cells[pos[0]][pos[1]] = value

    def update(self, tick):
        '''Update the game.

        If the player don't perform its move before a maximum amount of time 
        (``chess.config["max_move_time"]``), the player receive an infraction.

        :param tick: the time elapsed since the last update.
        :return: a boolean telling if the player received an infraction by
                 maximum time.
        '''
        self.move_time -= tick
        self.game_time += tick

        has_infractions = False

        if self.who_moves == chess.WHITE:
            self.white_time += tick
        else:
            self.black_time += tick

        if self.move_time <= 0:
            self.move_time = chess.config['max_move_time']

            if self.who_moves == chess.WHITE:
                self.white_infractions += 1
                if self.white_infractions >= chess.config['max_infractions']:
                    self.winner = chess.BLACK
            else:
                self.black_infractions += 1
                if self.black_infractions >= chess.config['max_infractions']:
                    self.winner = chess.WHITE

            has_infractions = True

        return has_infractions

    def move(self, from_pos, to_pos):
        '''Perform a move verifying the validity of the move.

        If the player tries to perform an invalid movement, the ``bad_move`` 
        flag is registered on the board state and an infraction is counted.

        :param from_pos: the current piece position.
        :param to_pos: the next position of the piece.
        '''
        from_piece = self[from_pos]
        to_piece = self[to_pos]

        # Change bad move state
        self.bad_move = False

        # Verify if it is a valid move
        if not self.is_valid_move(from_pos, to_pos):
            self.bad_move = True
            if self.who_moves == chess.BLACK:
                self.black_infractions += 1
            else:
                self.white_infractions += 1
            
            self.move_time = chess.config['max_move_time']
            self._verify_win()
            return

        # Verify if it is an enpassant capture
        if self.enpassant and from_piece.type == chess.PAWN:
            if to_pos[0] == self.enpassant[0] and to_pos[1] == self.enpassant[1]:
                to_piece = self.enpassant_piece

        # Verify if it is a capture (to remove from lists)
        if to_piece is not None:
            self.nocapture_moves = 0
            self.remove_piece(to_piece)
        else:
            self.nocapture_moves += 1

        # Clear enpassant state
        self.enpassant = None
        self.enpassant_piece = None

        # Change enpassant state, if possible
        if from_piece.type == chess.PAWN:
            d = abs(from_pos[0]-to_pos[0])
            left = self[to_pos[0], to_pos[1]-1]
            right = self[to_pos[0], to_pos[1]+1]

            has_left_pawn = (left is not None and \
                             left.type == chess.PAWN and \
                             left.team != from_piece.team)
            has_right_pawn = (right is not None and \
                              right.type == chess.PAWN and \
                              right.team != from_piece.team)

            if d == 2 and (has_left_pawn or has_right_pawn):
                row = (to_pos[0]+from_pos[0])//2
                col = to_pos[1]
                self.enpassant = (row, col)
                self.enpassant_piece = from_piece

        # Change who moves state
        if self.who_moves == chess.WHITE:
            self.who_moves = chess.BLACK
        else:
            self.who_moves = chess.WHITE

        # Change positions
        self[to_pos] = from_piece
        self[from_pos] = None
        from_piece.move_to(to_pos)#position = to_pos
        
        # Change time state
        self.move_time = chess.config['max_move_time']

        # Verify winning
        self._verify_win()
        if not self.winner:
            self._verify_tie()

        import pprint
        pprint.pprint(self.get_state())

    def raw_move(self, from_pos, to_pos):
        '''Perform a move without verifying the validity of the move.

        :param from_pos: the current piece position.
        :param to_pos: the next position of the piece.
        '''
        from_piece = self[from_pos]
        to_piece = self[to_pos]

        if to_piece is not None:
            self.remove_piece(to_piece)

        self[to_pos] = from_piece
        self[from_pos] = None
        from_piece.move_to(to_pos)

    def new_piece(self, type_, pos):
        '''Create and add a new piece to the board.

        :param type_: a string with the piece type, i.e., a character in 
                      ``"rbnpqk"``.
        :param pos: a 2-tuple with the board position.
        '''
        cls = PIECES[type_.lower()]
        team = chess.BLACK if type_.lower() == type_ else chess.WHITE

        piece = cls(self, team, pos)
        self._cells[pos[0]][pos[1]] = piece
        self.pieces.append(piece)
        if team == chess.BLACK:
            self.black_pieces.append(piece)
        else:
            self.white_pieces.append(piece)

    def remove_piece(self, piece):
        '''Remove a given piece from this board.
        '''
        pos = piece.position
        self[pos] = None

        self.pieces.remove(piece)
        if piece.team == chess.BLACK:
            self.black_pieces.remove(piece)
        else:
            self.white_pieces.remove(piece)

    def set_board(self, c):
        '''Given a string, sets the board configuration.

        :param c: a string with the board configuration.
        '''
        i = 0

        for row in xrange(7, -1, -1):
            for col in xrange(0, 8):
                if c[i] != '.':
                    self.new_piece(c[i], (row, col))

                i += 1

    def get_board(self):
        '''Return the board-string representation.

        :return: a string with the board representation.
        '''
        board = []
        for row in xrange(7, -1, -1):
            for col in xrange(0, 8):
                p = self[(row, col)]
                if p:
                    board.append(p.repr)
                else:
                    board.append('.')
        board = ''.join(board)
        return board

    def get_state(self):
        '''Return the board state as a dict.

        :return: state as a dict.
        '''
        return {
            'board': self.get_board(),
            'enpassant': self.enpassant,
            'who_moves': self.who_moves,
            'bad_move': self.bad_move,
            'white_infractions': self.white_infractions,
            'black_infractions': self.black_infractions,
            'winner': self.winner,
            '50moves': self.nocapture_moves >= 80,
            'draw': self.draw,
        }

    def is_valid_move(self, from_pos, to_pos):
        '''Verify if is valid to move a piece from one position to another.

        :param from_pos: the current piece position.
        :param to_pos: the destiny position of the piece.
        :return: a boolean.
        '''
        dest_row, dest_col = to_pos

        if not 0 <= dest_row <= 7 or not 0 <= dest_col <= 7:
            return False

        from_piece = self[from_pos]
        if from_piece is None:
            return False

        if from_piece.team != self.who_moves:
            return False

        if not from_piece.is_valid_move(to_pos):
            return False

        return True

    def is_empty(self, pos):
        '''Verify if a given position in the baord is empty.

        :param pos: 2-tuple with the board position.
        :return: a boolean.
        '''
        return self[pos] is None

    def is_enpassant(self, pos):
        '''Verify if enpassant is possible for a given position in the board.

        :param pos: 2-tuple with the board position.
        :return: a boolean.
        '''
        enp = self.enpassant
        return enp and enp[0] == pos[0] and enp[1] == pos[1]

    def pr(self):
        '''An auxiliar function to print the board.'''

        for row in xrange(7, -1, -1):
            for col in xrange(0, 8):
                p = self[(row, col)]
                if p:
                    print p.repr,
                else:
                    print '.',
            print


