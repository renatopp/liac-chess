import chess

__all__ = ['tie_nomove', 'tie_50moves']


def tie_nomove(board):
    if board.who_moves == chess.WHITE:
        pieces = board.white_pieces
    else:
        pieces = board.black_pieces

    for p in pieces:
        moves = p.generate()
        if moves:
            return False

    return True

def tie_50moves(board):
    if board.nocapture_moves >= 100:
        return True
        
    return False