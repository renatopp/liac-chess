import unittest
from .helpers import StubBoard, StubPiece, C, WHITE, BLACK

class TestQueenCapture(unittest.TestCase):
    def get_queen(self, board, team, position):
        from chess.models import Queen
        return Queen(board, team, position)

    # VALID CAPTURES ----------------------------------------------------------
    def test_valid_capture(self):
        board = StubBoard()
        board[C('e8')] = StubPiece(board, BLACK, C('e4'))
        queen = self.get_queen(board, WHITE, C('e4'))
        result = queen.is_valid_move(C('e8'))
        self.assertTrue(result)

        board = StubBoard()
        board[C('g4')] = StubPiece(board, WHITE, C('g4'))
        queen = self.get_queen(board, BLACK, C('e4'))
        result = queen.is_valid_move(C('g4'))
        self.assertTrue(result)
    # -------------------------------------------------------------------------

    # INVALID MOVES -----------------------------------------------------------
    def test_invalid_capturesameteam(self):
        board = StubBoard()
        board[C('e8')] = StubPiece(board, WHITE, C('e4'))
        queen = self.get_queen(board, WHITE, C('e4'))
        result = queen.is_valid_move(C('e8'))
        self.assertFalse(result)

        board = StubBoard()
        board[C('e8')] = StubPiece(board, BLACK, C('e4'))
        queen = self.get_queen(board, BLACK, C('e4'))
        result = queen.is_valid_move(C('e8'))
        self.assertFalse(result)
    # -------------------------------------------------------------------------

    # VALID CAPTURES ----------------------------------------------------------
    def test_valid_capture_diag(self):
        board = StubBoard()
        board[C('h7')] = StubPiece(board, BLACK, C('h7'))
        queen = self.get_queen(board, WHITE, C('e4'))
        result = queen.is_valid_move(C('h7'))
        self.assertTrue(result)

        board = StubBoard()
        board[C('b1')] = StubPiece(board, WHITE, C('b1'))
        queen = self.get_queen(board, BLACK, C('e4'))
        result = queen.is_valid_move(C('b1'))
        self.assertTrue(result)
    # -------------------------------------------------------------------------

    # INVALID MOVES -----------------------------------------------------------
    def test_invalid_capturesameteam_diag(self):
        board = StubBoard()
        board[C('h7')] = StubPiece(board, WHITE, C('h7'))
        queen = self.get_queen(board, WHITE, C('e4'))
        result = queen.is_valid_move(C('h7'))
        self.assertFalse(result)

        board = StubBoard()
        board[C('b1')] = StubPiece(board, BLACK, C('b1'))
        queen = self.get_queen(board, BLACK, C('e4'))
        result = queen.is_valid_move(C('b1'))
        self.assertFalse(result)
    # -------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()