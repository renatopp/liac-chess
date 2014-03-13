import unittest
from .helpers import C, WHITE, BLACK

class TestWinPawnCature(unittest.TestCase):
    def get_board(self, *args, **kwargs):
        from chess.models import Board
        return Board(*args, **kwargs)

    def get_win(self, *args, **kwargs):
        from chess.models import win_pawncapture
        return win_pawncapture(*args, **kwargs)

    def test_complete_nowin(self):
        config = 'r......r' + \
                 'pppppppp' + \
                 '........' + \
                 '........' + \
                 '........' + \
                 '........' + \
                 'PPPPPPPP' + \
                 'R......R' 
        board = self.get_board(config)

        result = self.get_win(board)
        self.assertEqual(result, 0)

    def test_single_nowin(self):
        config = 'r..r....' + \
                 '........' + \
                 '........' + \
                 '...p....' + \
                 '....P...' + \
                 '........' + \
                 '........' + \
                 'R......R' 
        board = self.get_board(config)

        result = self.get_win(board)
        self.assertEqual(result, 0)

    def test_single_whitewin(self):
        config = 'r..r....' + \
                 '........' + \
                 '........' + \
                 '...P....' + \
                 '........' + \
                 '........' + \
                 '........' + \
                 'R......R' 
        board = self.get_board(config)

        result = self.get_win(board)
        self.assertEqual(result, WHITE)

    def test_single_blackwin(self):
        config = 'r..r....' + \
                 '........' + \
                 '........' + \
                 '........' + \
                 '....p...' + \
                 '........' + \
                 '........' + \
                 'R......R' 
        board = self.get_board(config)

        result = self.get_win(board)
        self.assertEqual(result, BLACK)

if __name__ == '__main__':
    unittest.main()