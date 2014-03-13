import chess
from .pieces import *

__all__ = ['Board']

PIECES = {
    'p': Pawn,
    'r': Rook,
    'b': Bishop,
    'q': Queen,
    'n': Knight,
    # 'k': King,
}

class Board(object):
    def __init__(self, board='.'*64, win_methods=[], tie_methods=[], 
                 allow_enpassant=False, allow_castle=False, 
                 allow_rook_promotion=False, allow_queen_promotion=False,
                 allow_knight_promotion=False, allow_bishop_promotion=False):

        self.win_methods = self._get_win_methods(win_methods)
        self.tie_methods = self._get_tie_methods(tie_methods)

        self.allow_enpassant = allow_enpassant
        self.allow_castle = allow_castle
        self.allow_rook_promotion = allow_rook_promotion
        self.allow_queen_promotion = allow_queen_promotion
        self.allow_knight_promotion = allow_knight_promotion
        self.allow_bishop_promotion = allow_bishop_promotion

        self._cells = [[None for j in xrange(8)] for i in xrange(8)]
        self.pieces = []
        self.black_pieces = []
        self.white_pieces = []

        self.enpassant = None
        self.enpassant_piece = None

        self.white_has_queen_castle = False
        self.white_has_king_castle = False
        self.black_has_queen_castle = False
        self.black_has_king_castle = False

        self.black_in_check = False
        self.white_in_check = False

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

        self.set_board(board)

    def _get_win_methods(self, methods):
        r = []

        for method_name in methods:
            name = 'win_'+method_name
            if hasattr(chess.models, name):
                r.append(getattr(chess.models, name))
            else:
                raise ValueError('Win method "%s" not found.'%method_name)

        return r

    def _get_tie_methods(self, methods):
        r = []

        for method_name in methods:
            name = 'tie_'+method_name
            if hasattr(chess.models, name):
                r.append(getattr(chess.models, name))
            else:
                raise ValueError('Tie method "%s" not found.'%method_name)

        return r

    def update(self, tick):
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

    def is_valid_move(self, from_pos, to_pos):
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

    def _verify_win(self):
        for win in self.win_methods:
            r = win(self)
            if r != chess.NONE:
                self.winner = r
                return

    def _verify_tie(self):
        for tie in self.tie_methods:
            if tie(self):
                self.draw = True
                return

    def raw_move(self, from_pos, to_pos):
        from_piece = self[from_pos]
        to_piece = self[to_pos]

        if to_piece is not None:
            self.remove_piece(to_piece)

        self[to_pos] = from_piece
        self[from_pos] = None
        from_piece.move_to(to_pos)

    def move(self, from_pos, to_pos):
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

            has_left_pawn = (left is not None and left.type == chess.PAWN)
            has_right_pawn = (right is not None and right.type == chess.PAWN)

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

    def set_board(self, c):
        i = 0

        for row in xrange(7, -1, -1):
            for col in xrange(0, 8):
                if c[i] != '.':
                    self.new_piece(c[i], (row, col))

                i += 1

    def new_piece(self, type_, pos):
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
        pos = piece.position
        self[pos] = None

        self.pieces.remove(piece)
        if piece.team == chess.BLACK:
            self.black_pieces.remove(piece)
        else:
            self.white_pieces.remove(piece)

    def get_board(self):
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

    def __getitem__(self, pos):
        if not 0 <= pos[0] <= 7 or not 0 <= pos[1] <= 7:
            return None

        return self._cells[pos[0]][pos[1]]

    def __setitem__(self, pos, value):
        self._cells[pos[0]][pos[1]] = value

    def is_empty(self, pos):
        return self[pos] is None

    def is_enpassant(self, pos):
        enp = self.enpassant
        return enp and enp[0] == pos[0] and enp[1] == pos[1]

    def pr(self):
        for row in xrange(7, -1, -1):
            for col in xrange(0, 8):
                p = self[(row, col)]
                if p:
                    print p.repr,
                else:
                    print '.',
            print


