import unittest
from .case_board import BoardTestCase
from .helpers import C, WHITE, BLACK

class TestBoardMove(BoardTestCase):
    def get_board(self, *args, **kwargs):
        from chess.models import Board
        return Board(*args, **kwargs)

    def test_bad_move(self):
        config = 'r......r' + \
                 'pppppppp' + \
                 '........' + \
                 '........' + \
                 '........' + \
                 '........' + \
                 'PPPPPPPP' + \
                 'R......R' 
        board = self.get_board(config)

        piece = board[C('a1')]
        self.assertFalse(board.bad_move)
        board.move(C('a1'), C('a3'))
        self.assertTrue(board.bad_move)
        self.assertEqual(board[C('a1')], piece)
        self.assertEqual(board[C('a3')], None)

    def test_infractions(self):
        config = 'r......r' + \
                 'pppppppp' + \
                 '........' + \
                 '........' + \
                 '........' + \
                 '........' + \
                 'PPPPPPPP' + \
                 'R......R' 
        board = self.get_board(config)

        self.assertEqual(board.white_infractions, 0)
        board.move(C('a1'), C('a3'))
        self.assertEqual(board.white_infractions, 1)

    def test_simple_move(self):
        config = 'r......r' + \
                 'pppppppp' + \
                 '........' + \
                 '........' + \
                 '........' + \
                 '........' + \
                 'PPPPPPPP' + \
                 'R......R' 
        board = self.get_board(config)

        piece = board[C('e2')]
        board.move(C('e2'), C('e3'))
        self.assertEqual(board[C('e2')], None)
        self.assertEqual(board[C('e3')], piece)
        self.assertEqual(board[C('e3')].position[0], C('e3')[0])
        self.assertEqual(board[C('e3')].position[1], C('e3')[1])

    def test_who_moves(self):
        config = 'r......r' + \
                 'pppppppp' + \
                 '........' + \
                 '........' + \
                 '........' + \
                 '........' + \
                 'PPPPPPPP' + \
                 'R......R' 
        board = self.get_board(config)

        self.assertEqual(board.who_moves, WHITE)
        board.move(C('e2'), C('e3'))
        self.assertEqual(board.who_moves, BLACK)

    def test_enpassant_generation(self):
        config = 'r......r' + \
                 'pppppppp' + \
                 '........' + \
                 '...P....' + \
                 '........' + \
                 '........' + \
                 'PPP.PPPP' + \
                 'R......R' 
        board = self.get_board(config)
        board.who_moves = BLACK

        self.assertEqual(board[C('e5')], None)

        piece = board[C('e7')]
        board.move(C('e7'), C('e5'))

        self.assertNotEqual(board.enpassant, None)
        self.assertEqual(board.enpassant[0], C('e6')[0])
        self.assertEqual(board.enpassant[1], C('e6')[1])
        self.assertEqual(board.enpassant_piece, piece)

    # def test_enpassant_no_generation(self):
    #     config = 'r......r' + \
    #              'p.pppppp' + \
    #              '........' + \
    #              '.p......' + \
    #              'P.......' + \
    #              '........' + \
    #              '.PPPPPPP' + \
    #              'R......R' 
    #     board = self.get_board(config)
    #     board.who_moves = WHITE


    #     self.assertEqual(board[C('a5')], None)
    #     board.move(C('a4'), C('a5'))
    #     self.assertNotEqual(board[C('a5')], None)

    #     self.assertEqual(board.enpassant, None)
    #     # self.assertEqual(board.enpassant[0], C('e6')[0])
    #     # self.assertEqual(board.enpassant[1], C('e6')[1])
        # self.assertEqual(board.enpassant_piece, piece)

        


if __name__ == '__main__':
    unittest.main()