import unittest
from .case_board import BoardTestCase
from .helpers import C, WHITE, BLACK

class TestBoardValidateMoves(BoardTestCase):
    def get_board(self, *args, **kwargs):
        from chess.models import Board
        return Board(*args, **kwargs)

    def test_invalid_outofboard(self):
        board = self.get_board()

        result = board.is_valid_move(C('e2'), (3, 10))
        self.assertFalse(result)

        result = board.is_valid_move(C('e2'), (3, -1))
        self.assertFalse(result)

        result = board.is_valid_move(C('e2'), (-1, 3))
        self.assertFalse(result)

        result = board.is_valid_move(C('e2'), (15, 3))
        self.assertFalse(result)

    def test_invalid_piece(self):
        board = self.get_board()

        result = board.is_valid_move(C('e2'), C('e3'))
        self.assertFalse(result)

    def test_valid_piecemove(self):
        config = 'r......r' + \
                 'pppppppp' + \
                 '........' + \
                 '........' + \
                 '........' + \
                 '........' + \
                 'PPPPPPPP' + \
                 'R......R' 
        board = self.get_board(config)

        result = board.is_valid_move(C('e2'), C('e3'))
        self.assertTrue(result)


    def test_invalid_piecemove(self):
        config = 'r......r' + \
                 'pppppppp' + \
                 '........' + \
                 '........' + \
                 '........' + \
                 '........' + \
                 'PPPPPPPP' + \
                 'R......R' 
        board = self.get_board(config)

        result = board.is_valid_move(C('e2'), C('e5'))
        self.assertFalse(result)

        result = board.is_valid_move(C('a1'), C('a5'))
        self.assertFalse(result)

    def test_invalid_teampiece(self):
        config = 'r......r' + \
                 'pppppppp' + \
                 '........' + \
                 '........' + \
                 '........' + \
                 '........' + \
                 'PPPPPPPP' + \
                 'R......R' 
        board = self.get_board(config)

        piece = board[C('e7')]
        board.move(C('e7'), C('e6'))
        self.assertEqual(board[C('e6')], None)
        self.assertEqual(board[C('e7')], piece)
        self.assertTrue(board.bad_move)
        self.assertEqual(board.white_infractions, 1)



if __name__ == '__main__':
    unittest.main()