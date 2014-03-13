import chess

__all__ = ['win_pawncapture', 'win_pawnpromotion', 'win_maxinfractions']


def win_pawncapture(board):
    has_black_pawn = any([p.type == chess.PAWN for p in board.black_pieces])
    has_white_pawn = any([p.type == chess.PAWN for p in board.white_pieces])

    if not has_black_pawn:
        return chess.WHITE

    if not has_white_pawn:
        return chess.BLACK

    return chess.NONE

def win_pawnpromotion(board):
    for p in board.white_pieces:
        if p.type == chess.PAWN and p.position[0] == 7:
            return chess.WHITE

    for p in board.black_pieces:
        if p.type == chess.PAWN and p.position[0] == 0:
            return chess.BLACK

    return chess.NONE

def win_maxinfractions(board):
    max_infractions = chess.config['max_infractions']

    if board.black_infractions >= max_infractions:
        return chess.WHITE

    if board.white_infractions >= max_infractions:
        return chess.BLACK

    return chess.NONE