import unittest
from .helpers import StubBoard, StubPiece, C, WHITE, BLACK

class TestKnightMovement(unittest.TestCase):
    def get_knight(self, board, team, position):
        from chess.models import Knight
        return Knight(board, team, position)

    # VALID MOVES -------------------------------------------------------------
    def test_valid_toprighttop(self):
        board = StubBoard()

        knight = self.get_knight(board, WHITE, C('e4'))
        result = knight.is_valid_move(C('f6'))
        self.assertTrue(result)

    def test_valid_toprightbottom(self):
        board = StubBoard()

        knight = self.get_knight(board, WHITE, C('e4'))
        result = knight.is_valid_move(C('g5'))
        self.assertTrue(result)

    def test_valid_toplefttop(self):
        board = StubBoard()

        knight = self.get_knight(board, WHITE, C('e4'))
        result = knight.is_valid_move(C('d6'))
        self.assertTrue(result)

    def test_valid_topleftbottom(self):
        board = StubBoard()

        knight = self.get_knight(board, WHITE, C('e4'))
        result = knight.is_valid_move(C('c5'))
        self.assertTrue(result)

    def test_valid_bottomlefttop(self):
        board = StubBoard()

        knight = self.get_knight(board, WHITE, C('e4'))
        result = knight.is_valid_move(C('c3'))
        self.assertTrue(result)

    def test_valid_bottomleftbottom(self):
        board = StubBoard()

        knight = self.get_knight(board, WHITE, C('e4'))
        result = knight.is_valid_move(C('d2'))
        self.assertTrue(result)

    def test_valid_bottomrighttop(self):
        board = StubBoard()

        knight = self.get_knight(board, WHITE, C('e4'))
        result = knight.is_valid_move(C('f2'))
        self.assertTrue(result)

    def test_valid_bottomrightbottom(self):
        board = StubBoard()

        knight = self.get_knight(board, WHITE, C('e4'))
        result = knight.is_valid_move(C('g3'))
        self.assertTrue(result)
    # -------------------------------------------------------------------------

    # INVALID MOVES -----------------------------------------------------------
    def test_invalid(self):
        board = StubBoard()

        knight = self.get_knight(board, WHITE, C('e4'))
        result = knight.is_valid_move(C('e6'))
        self.assertFalse(result)

    def test_invalid_samepos(self):
        board = StubBoard()

        knight = self.get_knight(board, WHITE, C('e4'))
        result = knight.is_valid_move(C('e4'))
        self.assertFalse(result)
    # -------------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()