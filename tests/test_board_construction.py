import unittest
from .case_board import BoardTestCase
from .helpers import C, WHITE, BLACK

class TestBoardConstruction(BoardTestCase):
    def get_board(self, *args, **kwargs):
        from chess.models import Board
        return Board(*args, **kwargs)

    def test_empty(self):
        board = self.get_board()

        for row in xrange(8):
            for col in xrange(8):
                piece = board[(row, col)]
                self.assertEqual(piece, None)

    def test_pawnbattle(self):
        config = 'r......rpppppppp................................PPPPPPPPR......R'
        board = self.get_board(config)

        i = 0
        for row in xrange(7, -1, -1):
            for col in xrange(0, 8):
                piece = board[(row, col)]

                if config[i] == '.':
                    self.assertEqual(piece, None)
                else:
                    self.assertEqual(piece.repr, config[i])

                i += 1

        state = board.get_state()

        self.assertEqual(state['board'], config)

if __name__ == '__main__':
    unittest.main()