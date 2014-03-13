import unittest
from .case_board import BoardTestCase
from .helpers import C, WHITE, BLACK, NONE


def stub_tie_position(board):
    piece = board[C('e5')]
    if piece is not None:
        return True

    return False

class TestBoardTie(BoardTestCase):
    def get_board(self, *args, **kwargs):
        from chess.models import Board
        return Board(*args, **kwargs)

    def test_notie(self):
        config = '........' + \
                 '........' + \
                 '....p...' + \
                 '........' + \
                 '........' + \
                 '....P...' + \
                 '........' + \
                 '........' 
        board = self.get_board(config)
        board.tie_methods = [stub_tie_position]

        self.assertFalse(board.draw)
        board.move(C('e3'), C('e4'))
        self.assertFalse(board.draw)

    def test_tie(self):
        config = '........' + \
                 '........' + \
                 '....p...' + \
                 '........' + \
                 '....P...' + \
                 '........' + \
                 '........' + \
                 '........' 
        board = self.get_board(config)
        board.tie_methods = [stub_tie_position]

        self.assertFalse(board.draw)
        board.move(C('e4'), C('e5'))
        self.assertTrue(board.draw)


if __name__ == '__main__':
    unittest.main()