import unittest
from .helpers import StubBoard, StubPiece, C, WHITE, BLACK

class TestPawnMovement(unittest.TestCase):
    def get_pawn(self, board, team, position):
        from chess.models import Pawn
        return Pawn(board, team, position)

    # VALID MOVES -------------------------------------------------------------
    def test_valid_1forward(self):
        board = StubBoard()
        pawn = self.get_pawn(board, WHITE, C('e2'))
        result = pawn.is_valid_move(C('e3'))
        self.assertTrue(result)

        pawn = self.get_pawn(board, BLACK, C('e7'))
        result = pawn.is_valid_move(C('e6'))
        self.assertTrue(result)

    def test_valid_2forward(self):
        board = StubBoard()
        pawn = self.get_pawn(board, WHITE, C('e2'))
        result = pawn.is_valid_move(C('e4'))
        self.assertTrue(result)

        pawn = self.get_pawn(board, BLACK, C('e7'))
        result = pawn.is_valid_move(C('e5'))
        self.assertTrue(result)
    # -------------------------------------------------------------------------

    # INVALID MOVES -----------------------------------------------------------
    def test_invalid_wrongcolumn(self):
        board = StubBoard()
        pawn = self.get_pawn(board, WHITE, C('e2'))
        result = pawn.is_valid_move(C('d3'))
        self.assertFalse(result)

        result = pawn.is_valid_move(C('f3'))
        self.assertFalse(result)

        pawn = self.get_pawn(board, BLACK, C('e7'))
        result = pawn.is_valid_move(C('d5'))
        self.assertFalse(result)

        result = pawn.is_valid_move(C('a1'))
        self.assertFalse(result)

    def test_invalid_2moreforward(self):
        board = StubBoard()
        pawn = self.get_pawn(board, WHITE, C('e2'))
        result = pawn.is_valid_move(C('e5'))
        self.assertFalse(result)

        pawn = self.get_pawn(board, BLACK, C('e7'))
        result = pawn.is_valid_move(C('e4'))
        self.assertFalse(result)

    def test_invalid_backwardmove(self):
        board = StubBoard()
        pawn = self.get_pawn(board, WHITE, C('g5'))
        result = pawn.is_valid_move(C('g4'))
        self.assertFalse(result)

        pawn = self.get_pawn(board, BLACK, C('g4'))
        result = pawn.is_valid_move(C('g5'))
        self.assertFalse(result)

    def test_invalid_2forward(self):
        board = StubBoard()
        pawn = self.get_pawn(board, WHITE, C('d2'))
        pawn.move_to(C('d4'))
        result = pawn.is_valid_move(C('d6'))
        self.assertFalse(result)

        pawn = self.get_pawn(board, BLACK, C('d6'))
        pawn.move_to(C('d5'))
        result = pawn.is_valid_move(C('d3'))
        self.assertFalse(result)

    def test_invalid_sameposition(self):
        board = StubBoard()
        pawn = self.get_pawn(board, WHITE, C('d2'))
        result = pawn.is_valid_move(C('d2'))
        self.assertFalse(result)

        pawn = self.get_pawn(board, BLACK, C('d2'))
        result = pawn.is_valid_move(C('d2'))
        self.assertFalse(result)
    # -------------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()