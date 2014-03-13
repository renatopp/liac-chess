import unittest
from .helpers import StubBoard, StubPiece, C, WHITE, BLACK

class TestPawnCapture(unittest.TestCase):
    def get_pawn(self, board, team, position):
        from chess.models import Pawn
        return Pawn(board, team, position)

    def test_valid_capture(self):
        board = StubBoard()
        board[C('d3')] = StubPiece(board, BLACK, C('d3'))
        board[C('f3')] = StubPiece(board, BLACK, C('f3'))

        pawn = self.get_pawn(board, WHITE, C('e2'))

        result = pawn.is_valid_move(C('d3'))
        self.assertTrue(result)

        result = pawn.is_valid_move(C('f3'))
        self.assertTrue(result)

        board = StubBoard()
        board[C('b6')] = StubPiece(board, WHITE, C('b6'))
        board[C('d6')] = StubPiece(board, WHITE, C('d6'))

        pawn = self.get_pawn(board, BLACK, C('c7'))

        result = pawn.is_valid_move(C('b6'))
        self.assertTrue(result)

        result = pawn.is_valid_move(C('d6'))
        self.assertTrue(result)

    def test_invalid_captureforward(self):
        board = StubBoard()
        board[C('e3')] = StubPiece(board, BLACK, C('e3'))
        pawn = self.get_pawn(board, WHITE, C('e2'))
        result = pawn.is_valid_move(C('e3'))
        self.assertFalse(result)

        board = StubBoard()
        board[C('e5')] = StubPiece(board, WHITE, C('e5'))
        pawn = self.get_pawn(board, BLACK, C('e6'))
        result = pawn.is_valid_move(C('e5'))
        self.assertFalse(result)

    def test_invalid_capturebackward(self):
        board = StubBoard()
        board[C('e3')] = StubPiece(board, BLACK, C('e3'))
        pawn = self.get_pawn(board, WHITE, C('d4'))
        result = pawn.is_valid_move(C('e3'))
        self.assertFalse(result)

        board = StubBoard()
        board[C('e5')] = StubPiece(board, WHITE, C('e5'))
        pawn = self.get_pawn(board, BLACK, C('d7'))
        result = pawn.is_valid_move(C('e5'))
        self.assertFalse(result)

    def test_invalid_capturedistant(self):
        board = StubBoard()
        board[C('c4')] = StubPiece(board, BLACK, C('c4'))
        pawn = self.get_pawn(board, WHITE, C('e2'))
        result = pawn.is_valid_move(C('c4'))
        self.assertFalse(result)

        board = StubBoard()
        board[C('a4')] = StubPiece(board, WHITE, C('a4'))
        pawn = self.get_pawn(board, BLACK, C('c7'))
        result = pawn.is_valid_move(C('a4'))
        self.assertFalse(result)

    def test_invalid_capturesameteam(self):
        board = StubBoard()
        board[C('c4')] = StubPiece(board, WHITE, C('c4'))
        pawn = self.get_pawn(board, WHITE, C('d3'))
        result = pawn.is_valid_move(C('c4'))
        self.assertFalse(result)

        board = StubBoard()
        board[C('a4')] = StubPiece(board, BLACK, C('a5'))
        pawn = self.get_pawn(board, BLACK, C('b6'))
        result = pawn.is_valid_move(C('a5'))
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()