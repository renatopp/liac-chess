import unittest
from .case_board import BoardTestCase
from .helpers import C, WHITE, BLACK, NONE

class TestBoardMove(BoardTestCase):
    def get_board(self, *args, **kwargs):
        from chess.models import Board
        return Board(*args, **kwargs)

    def test_stateitems(self):
        board = self.get_board()

        result = board.get_state()
        self.assertTrue('board' in result)
        self.assertTrue('enpassant' in result)
        self.assertTrue('who_moves' in result)
        self.assertTrue('bad_move' in result)
        self.assertTrue('white_infractions' in result)
        self.assertTrue('black_infractions' in result)
        self.assertTrue('winner' in result)
        self.assertTrue('50moves' in result)
        self.assertTrue('draw' in result)

    def test_simplestate(self):
        board = self.get_board()

        result = board.get_state()
        self.assertEqual(result['board'], '.'*64)
        self.assertEqual(result['who_moves'], WHITE)
        self.assertEqual(result['white_infractions'], 0)
        self.assertEqual(result['white_infractions'], 0)
        self.assertEqual(result['bad_move'], False)
        self.assertEqual(result['enpassant'], None)
        self.assertEqual(result['winner'], NONE)
        self.assertEqual(result['50moves'], False)
        self.assertEqual(result['draw'], False)

    def test_completestate(self):
        config = 'r......r' + \
                 'pppppppp' + \
                 '........' + \
                 '........' + \
                 '........' + \
                 '........' + \
                 'PPPPPPPP' + \
                 'R......R' 
        board = self.get_board(config)
        board.who_moves = BLACK
        board.white_infractions = 40
        board.black_infractions = 10
        board.bad_move = True
        board.enpassant = C('g4')
        board.winner = BLACK
        board.nocapture_moves = 80
        board.draw = True

        result = board.get_state()
        self.assertEqual(result['board'], config)
        self.assertEqual(result['who_moves'], BLACK)
        self.assertEqual(result['white_infractions'], 40)
        self.assertEqual(result['black_infractions'], 10)
        self.assertEqual(result['bad_move'], True)
        self.assertEqual(result['enpassant'][0], 3)
        self.assertEqual(result['enpassant'][1], 6)
        self.assertEqual(result['winner'], BLACK)
        self.assertEqual(result['50moves'], True)
        self.assertEqual(result['draw'], True)

    def test_losing_enpassant(self):
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

        board.move(C('e2'), C('e4'))
        self.assertEqual(board.enpassant, None)
        self.assertEqual(board.enpassant_piece, None)


    def test_losing_badmove(self):
        config = 'r......r' + \
                 'pppp.ppp' + \
                 '........' + \
                 '...Pp...' + \
                 '........' + \
                 '........' + \
                 'PPP.PPPP' + \
                 'R......R' 
        board = self.get_board(config)

        board.bad_move = True

        board.move(C('e2'), C('e4'))
        self.assertFalse(board.bad_move)


if __name__ == '__main__':
    unittest.main()