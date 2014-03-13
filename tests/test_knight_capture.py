import unittest
from .helpers import StubBoard, StubPiece, C, WHITE, BLACK

class TestKnightMovement(unittest.TestCase):
    def get_knight(self, board, team, position):
        from chess.models import Knight
        return Knight(board, team, position)

    # VALID MOVES -------------------------------------------------------------
    def test_valid_capture(self):
        board = StubBoard()
        board[C('f6')] = StubPiece(board, BLACK, C('f6'))

        knight = self.get_knight(board, WHITE, C('e4'))
        result = knight.is_valid_move(C('f6'))
        self.assertTrue(result)
    # -------------------------------------------------------------------------

    # INVALID MOVES -----------------------------------------------------------
    def test_invalid_capture(self):
        board = StubBoard()
        board[C('f6')] = StubPiece(board, BLACK, C('f6'))

        knight = self.get_knight(board, BLACK, C('e4'))
        result = knight.is_valid_move(C('f6'))
        self.assertFalse(result)
    # -------------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()