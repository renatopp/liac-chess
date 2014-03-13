import unittest
from .helpers import StubBoard, StubPiece, C, WHITE, BLACK

class TestBishopCapture(unittest.TestCase):
    def get_bishop(self, board, team, position):
        from chess.models import Bishop
        return Bishop(board, team, position)

    # VALID CAPTURES ----------------------------------------------------------
    def test_valid_capture(self):
        board = StubBoard()
        board[C('h7')] = StubPiece(board, BLACK, C('h7'))
        bishop = self.get_bishop(board, WHITE, C('e4'))
        result = bishop.is_valid_move(C('h7'))
        self.assertTrue(result)

        board = StubBoard()
        board[C('b1')] = StubPiece(board, WHITE, C('b1'))
        bishop = self.get_bishop(board, BLACK, C('e4'))
        result = bishop.is_valid_move(C('b1'))
        self.assertTrue(result)
    # -------------------------------------------------------------------------

    # INVALID MOVES -----------------------------------------------------------
    def test_invalid_capturesameteam(self):
        board = StubBoard()
        board[C('h7')] = StubPiece(board, WHITE, C('h7'))
        bishop = self.get_bishop(board, WHITE, C('e4'))
        result = bishop.is_valid_move(C('h7'))
        self.assertFalse(result)

        board = StubBoard()
        board[C('b1')] = StubPiece(board, BLACK, C('b1'))
        bishop = self.get_bishop(board, BLACK, C('e4'))
        result = bishop.is_valid_move(C('b1'))
        self.assertFalse(result)
    # -------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()