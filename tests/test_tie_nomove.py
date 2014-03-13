import unittest
from .helpers import C, WHITE, BLACK, NONE

class TestTieNoMove(unittest.TestCase):
    def get_board(self, *args, **kwargs):
        from chess.models import Board
        return Board(*args, **kwargs)

    def get_tie(self, *args, **kwargs):
        from chess.models import tie_nomove
        return tie_nomove(*args, **kwargs)

    def test_whitenotie(self):
        config = '........' + \
                 '........' + \
                 '........' + \
                 '.....p..' + \
                 '........' + \
                 '.....P..' + \
                 '........' + \
                 '........' 
        board = self.get_board(config)

        result = self.get_tie(board)
        self.assertFalse(result)

    def test_blacknotie(self):
        config = '........' + \
                 '........' + \
                 '........' + \
                 '........' + \
                 '......p.' + \
                 '.......P' + \
                 '........' + \
                 '........' 
        board = self.get_board(config)
        board.who_moves = BLACK

        result = self.get_tie(board)
        self.assertFalse(result)

    def test_whitetie(self):
        config = '........' + \
                 '........' + \
                 '........' + \
                 '.....p..' + \
                 '.....P..' + \
                 '........' + \
                 '........' + \
                 '........' 
        board = self.get_board(config)

        result = self.get_tie(board)
        self.assertTrue(result)

    def test_blacktie(self):
        config = '........' + \
                 '........' + \
                 '........' + \
                 '.....p..' + \
                 '.....P..' + \
                 '........' + \
                 '........' + \
                 '........' 
        board = self.get_board(config)
        board.who_moves = BLACK

        result = self.get_tie(board)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()