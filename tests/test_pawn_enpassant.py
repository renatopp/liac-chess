import unittest
from .helpers import StubBoard, StubPiece, C, WHITE, BLACK

class TestPawnEnPassant(unittest.TestCase):
    def get_pawn(self, board, team, position):
        from chess.models import Pawn
        return Pawn(board, team, position)

    def test_valid_enpassant(self):
        board = StubBoard()
        board.enpassant = C('c6')
        board[C('c5')] = StubPiece(board, BLACK, C('c5'))

        pawn = self.get_pawn(board, WHITE, C('b5'))
        result = pawn.is_valid_move(C('c6'))
        self.assertTrue(result)

        pawn = self.get_pawn(board, WHITE, C('d5'))
        result = pawn.is_valid_move(C('c6'))
        self.assertTrue(result)

        board = StubBoard()
        board.enpassant = C('e3')
        board[C('e4')] = StubPiece(board, WHITE, C('e4'))

        pawn = self.get_pawn(board, BLACK, C('d4'))
        result = pawn.is_valid_move(C('e3'))
        self.assertTrue(result)

        pawn = self.get_pawn(board, BLACK, C('f4'))
        result = pawn.is_valid_move(C('e3'))
        self.assertTrue(result)


    def test_invalid_enpassant_position(self):
        board = StubBoard()
        board.enpassant = C('c6')
        board[C('c5')] = StubPiece(board, BLACK, C('c5'))

        pawn = self.get_pawn(board, WHITE, C('a5'))
        result = pawn.is_valid_move(C('c6'))
        self.assertFalse(result)

        pawn = self.get_pawn(board, WHITE, C('e5'))
        result = pawn.is_valid_move(C('c6'))
        self.assertFalse(result)

        board = StubBoard()
        board.enpassant = C('e3')
        board[C('e4')] = StubPiece(board, WHITE, C('e4'))

        pawn = self.get_pawn(board, BLACK, C('c4'))
        result = pawn.is_valid_move(C('e3'))
        self.assertFalse(result)

        pawn = self.get_pawn(board, BLACK, C('g4'))
        result = pawn.is_valid_move(C('e3'))
        self.assertFalse(result)

    def test_invalid_enpassant_noempassant(self):
        board = StubBoard()
        board.enpassant = None
        board[C('c5')] = StubPiece(board, BLACK, C('c5'))

        pawn = self.get_pawn(board, WHITE, C('b5'))
        result = pawn.is_valid_move(C('c6'))
        self.assertFalse(result)

        pawn = self.get_pawn(board, WHITE, C('d5'))
        result = pawn.is_valid_move(C('c6'))
        self.assertFalse(result)


        board = StubBoard()
        board.enpassant = None
        board[C('e4')] = StubPiece(board, WHITE, C('e4'))

        pawn = self.get_pawn(board, BLACK, C('d4'))
        result = pawn.is_valid_move(C('e3'))
        self.assertFalse(result)

        pawn = self.get_pawn(board, BLACK, C('f4'))
        result = pawn.is_valid_move(C('e3'))
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()