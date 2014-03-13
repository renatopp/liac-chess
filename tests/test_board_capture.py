import unittest
from .case_board import BoardTestCase
from .helpers import C, WHITE, BLACK

class TestBoardCapture(BoardTestCase):
    def get_board(self, *args, **kwargs):
        from chess.models import Board
        return Board(*args, **kwargs)

    def test_simple_capture(self):
        config = 'r......r' + \
                 'pppppppp' + \
                 '........' + \
                 '........' + \
                 '........' + \
                 '........' + \
                 'PPPPPPP.' + \
                 'R......R' 
        board = self.get_board(config)

        enemy_pawn = board[C('h7')]
        self.assertTrue(enemy_pawn in board.pieces)
        self.assertTrue(enemy_pawn in board.black_pieces)

        piece = board[C('h1')]
        board.move(C('h1'), C('h7'))
        self.assertFalse(board.bad_move)
        self.assertEqual(board[C('h7')], piece)
        self.assertEqual(board[C('h1')], None)

        self.assertEqual(board.who_moves, BLACK)
        
        piece = board[C('h8')]
        board.move(C('h8'), C('h7'))
        self.assertFalse(board.bad_move)
        self.assertEqual(board[C('h7')], piece)
        self.assertEqual(board[C('h8')], None)

        self.assertTrue(enemy_pawn not in board.pieces)
        self.assertTrue(enemy_pawn not in board.black_pieces)


    def test_enpassant_capture(self):
        config = 'r......r' + \
                 'pppp.ppp' + \
                 '........' + \
                 '...Pp...' + \
                 '........' + \
                 '........' + \
                 'PPP.PPPP' + \
                 'R......R' 
        board = self.get_board(config)

        board.enpassant = C('e6')
        board.enpassant_piece = board[C('e5')]

        piece = board[C('d5')]
        board.move(C('d5'), C('e6'))

        self.assertEqual(board[C('e5')], None)
        self.assertEqual(board[C('d5')], None)
        self.assertEqual(board[C('e6')], piece)


if __name__ == '__main__':
    unittest.main()