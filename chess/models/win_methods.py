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

'''Collection of functions used to verify the end game condition (in the case
of a winner).

All functions here receive a ``Board`` instance and return the player who won 
the game, i.e.: ``chess.BLACK``, ``chess.WHITE`` or ``chess.NONE``.
'''

import chess

__all__ = ['win_pawncapture', 'win_pawnpromotion', 'win_maxinfractions']

def win_pawncapture(board):
    '''A player win the game when all the oppenent's pawns are captured.

    :param board: a ``Board`` instance.
    :return: the player who won the game or ``chess.NONE``.
    '''

    has_black_pawn = any([p.type == chess.PAWN for p in board.black_pieces])
    has_white_pawn = any([p.type == chess.PAWN for p in board.white_pieces])

    if not has_black_pawn:
        return chess.WHITE

    if not has_white_pawn:
        return chess.BLACK

    return chess.NONE

def win_pawnpromotion(board):
    '''A player win the game when one of its pawn has been promoted.

    :param board: a ``Board`` instance.
    :return: the player who won the game or ``chess.NONE``.
    '''

    for p in board.white_pieces:
        if p.type == chess.PAWN and p.position[0] == 7:
            return chess.WHITE

    for p in board.black_pieces:
        if p.type == chess.PAWN and p.position[0] == 0:
            return chess.BLACK

    return chess.NONE

def win_maxinfractions(board):
    '''A player win the game when the oppenent have more infractions than 
    ``chess.config['max_infractions']``.

    :param board: a ``Board`` instance.
    :return: the player who won the game or ``chess.NONE``.
    '''

    max_infractions = chess.config['max_infractions']

    if board.black_infractions >= max_infractions:
        return chess.WHITE

    if board.white_infractions >= max_infractions:
        return chess.BLACK

    return chess.NONE