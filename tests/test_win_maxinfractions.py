import unittest
from .helpers import C, WHITE, BLACK, NONE

class TestWinMaxInfractions(unittest.TestCase):
    def setUp(self):
        import chess
        chess.config = {
            "slot_0_ip": "",
            "slot_0_port": 50100,
            "slot_1_ip": "",
            "slot_1_port": 50200,
            "update_frequency": 10,
            "max_move_time": 5.9,
            "max_infractions": 10
        }

    def get_board(self, *args, **kwargs):
        from chess.models import Board
        return Board(*args, **kwargs)

    def get_win(self, *args, **kwargs):
        from chess.models import win_maxinfractions
        return win_maxinfractions(*args, **kwargs)

    def test_nowin(self):
        config = 'r......r' + \
                 'pppppppp' + \
                 '........' + \
                 '........' + \
                 '........' + \
                 '........' + \
                 'PPPPPPPP' + \
                 'R......R' 
        board = self.get_board(config)
        board.white_infractions = 9
        board.black_infractions = 9

        result = self.get_win(board)
        self.assertEqual(result, NONE)
        
    def test_whitewin(self):
        config = 'r......r' + \
                 'pppppppp' + \
                 '........' + \
                 '........' + \
                 '........' + \
                 '........' + \
                 'PPPPPPPP' + \
                 'R......R' 
        board = self.get_board(config)
        board.white_infractions = 9
        board.black_infractions = 10

        result = self.get_win(board)
        self.assertEqual(result, WHITE)

    def test_blackwin(self):
        config = 'r......r' + \
                 'pppppppp' + \
                 '........' + \
                 '........' + \
                 '........' + \
                 '........' + \
                 'PPPPPPPP' + \
                 'R......R' 
        board = self.get_board(config)
        board.white_infractions = 10
        board.black_infractions = 9

        result = self.get_win(board)
        self.assertEqual(result, BLACK)





if __name__ == '__main__':
    unittest.main()