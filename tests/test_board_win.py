import unittest
from .case_board import BoardTestCase
from .helpers import C, WHITE, BLACK, NONE


def stub_win_position(board):
    piece = board[C('e5')]
    if piece is not None:
        if piece.repr == 'R':
            return WHITE
        elif piece.repr == 'p':
            return BLACK

    return 0

def stub_win_infraction(board):
    max_infractions = 10

    if board.black_infractions >= max_infractions:
        return WHITE

    if board.white_infractions >= max_infractions:
        return BLACK

    return NONE

class TestBoardWin(BoardTestCase):
    def set_max_infractions(self, n):
        import chess
        chess.config = {}
        chess.config['max_infractions'] = n

    def get_board(self, *args, **kwargs):
        from chess.models import Board
        return Board(*args, **kwargs)

    def test_move_nowin(self):
        config = 'r......r' + \
                 'pppppppp' + \
                 '........' + \
                 '.......R' + \
                 '........' + \
                 '........' + \
                 'PPPPPPPP' + \
                 'R.......' 
        board = self.get_board(config)
        board.win_methods = [stub_win_position]

        self.assertEqual(board.winner, NONE)
        board.move(C('h5'), C('d5'))
        self.assertEqual(board.winner, NONE)

    def test_move_whitewin(self):
        config = 'r......r' + \
                 'pppppppp' + \
                 '........' + \
                 '.......R' + \
                 '........' + \
                 '........' + \
                 'PPPPPPPP' + \
                 'R.......' 
        board = self.get_board(config)
        board.win_methods = [stub_win_position]

        self.assertEqual(board.winner, NONE)
        board.move(C('h5'), C('e5'))
        self.assertEqual(board.winner, WHITE)

    def test_move_blackwin(self):
        config = 'r......r' + \
                 'pppppppp' + \
                 '........' + \
                 '.......R' + \
                 '........' + \
                 '........' + \
                 'PPPPPPPP' + \
                 'R.......' 
        board = self.get_board(config)
        board.win_methods = [stub_win_position]
        board.who_moves = BLACK

        self.assertEqual(board.winner, NONE)
        board.move(C('e7'), C('e5'))
        self.assertEqual(board.winner, BLACK)

    def test_infraction_whitewin(self):
        config = 'r......r' + \
                 'pppppppp' + \
                 '........' + \
                 '.......R' + \
                 '........' + \
                 '........' + \
                 'PPPPPPPP' + \
                 'R.......' 

        board = self.get_board(config)
        board.win_methods = [stub_win_infraction]
        board.white_infractions = 9
        board.black_infractions = 9

        self.assertEqual(board.winner, NONE)
        self.assertEqual(board.white_infractions, 9)
        board.move(C('e2'), C('a1'))
        self.assertEqual(board.white_infractions, 10)
        self.assertEqual(board.winner, BLACK)

    def test_infraction_whitewin(self):
        config = 'r......r' + \
                 'pppppppp' + \
                 '........' + \
                 '.......R' + \
                 '........' + \
                 '........' + \
                 'PPPPPPPP' + \
                 'R.......' 

        board = self.get_board(config)
        board.win_methods = [stub_win_infraction]
        board.who_moves = BLACK
        board.white_infractions = 9
        board.black_infractions = 9

        self.assertEqual(board.winner, NONE)
        self.assertEqual(board.black_infractions, 9)
        board.move(C('e2'), C('a1'))
        self.assertEqual(board.black_infractions, 10)
        self.assertEqual(board.winner, WHITE)


if __name__ == '__main__':
    unittest.main()