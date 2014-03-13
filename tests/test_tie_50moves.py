import unittest
from .helpers import C, WHITE, BLACK, NONE

class TestTie50Moves(unittest.TestCase):
    def get_board(self, *args, **kwargs):
        from chess.models import Board
        return Board(*args, **kwargs)

    def get_tie(self, *args, **kwargs):
        from chess.models import tie_50moves
        return tie_50moves(*args, **kwargs)

    def test_notie(self):
        config = '........' + \
                 '.......r' + \
                 '........' + \
                 '.......p' + \
                 '.......P' + \
                 '........' + \
                 '.......R' + \
                 '........' 
        board = self.get_board(config)
        board.nocapture_moves = 99

        result = self.get_tie(board)
        self.assertFalse(result)

    def test_tie(self):
        config = '........' + \
                 '.......r' + \
                 '........' + \
                 '.......p' + \
                 '.......P' + \
                 '........' + \
                 '.......R' + \
                 '........' 
        board = self.get_board(config)
        board.nocapture_moves = 100

        result = self.get_tie(board)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()