import unittest
from .helpers import StubBoard, StubPiece, C, WHITE, BLACK

class TestRookCapture(unittest.TestCase):
    def get_rook(self, board, team, position):
        from chess.models import Rook
        return Rook(board, team, position)

    # VALID CAPTURES ----------------------------------------------------------
    def test_valid_capture(self):
        board = StubBoard()
        board[C('e8')] = StubPiece(board, BLACK, C('e4'))
        rook = self.get_rook(board, WHITE, C('e4'))
        result = rook.is_valid_move(C('e8'))
        self.assertTrue(result)

        board = StubBoard()
        board[C('g4')] = StubPiece(board, WHITE, C('g4'))
        rook = self.get_rook(board, BLACK, C('e4'))
        result = rook.is_valid_move(C('g4'))
        self.assertTrue(result)
    # -------------------------------------------------------------------------

    # INVALID MOVES -----------------------------------------------------------
    def test_invalid_capturesameteam(self):
        board = StubBoard()
        board[C('e8')] = StubPiece(board, WHITE, C('e4'))
        rook = self.get_rook(board, WHITE, C('e4'))
        result = rook.is_valid_move(C('e8'))
        self.assertFalse(result)

        board = StubBoard()
        board[C('e8')] = StubPiece(board, BLACK, C('e4'))
        rook = self.get_rook(board, BLACK, C('e4'))
        result = rook.is_valid_move(C('e8'))
        self.assertFalse(result)
    # -------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()