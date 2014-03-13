import unittest
from .helpers import StubBoard, StubPiece, C, WHITE, BLACK

class TestQueenMovement(unittest.TestCase):
    def get_queen(self, board, team, position):
        from chess.models import Queen
        return Queen(board, team, position)

    # VALID MOVES -------------------------------------------------------------
    def test_valid_vertical(self):
        board = StubBoard()

        # Top
        queen = self.get_queen(board, WHITE, C('e4'))
        result = queen.is_valid_move(C('e8'))
        self.assertTrue(result)

        # Bottom
        queen = self.get_queen(board, WHITE, C('e4'))
        result = queen.is_valid_move(C('e1'))
        self.assertTrue(result)

    def test_valid_horizontal(self):
        board = StubBoard()

        # Right
        queen = self.get_queen(board, WHITE, C('e4'))
        result = queen.is_valid_move(C('h4'))
        self.assertTrue(result)

        # Left
        queen = self.get_queen(board, WHITE, C('e4'))
        result = queen.is_valid_move(C('a4'))
        self.assertTrue(result)
    # -------------------------------------------------------------------------

    # INVALID MOVES -----------------------------------------------------------
    def test_invalid_obstructedvertical(self):
        board = StubBoard()
        board[C('e7')] = StubPiece(board, WHITE, C('e7'))
        board[C('e2')] = StubPiece(board, WHITE, C('e2'))

        # Top
        queen = self.get_queen(board, BLACK, C('e4'))
        result = queen.is_valid_move(C('e8'))
        self.assertFalse(result)

        # Bottom
        queen = self.get_queen(board, BLACK, C('e4'))
        result = queen.is_valid_move(C('e1'))
        self.assertFalse(result)

    def test_invalid_obstructedhorizontal(self):
        board = StubBoard()
        board[C('g4')] = StubPiece(board, WHITE, C('g4'))
        board[C('b4')] = StubPiece(board, WHITE, C('b4'))

        # Right
        queen = self.get_queen(board, WHITE, C('e4'))
        result = queen.is_valid_move(C('h4'))
        self.assertFalse(result)

        # Left
        queen = self.get_queen(board, WHITE, C('e4'))
        result = queen.is_valid_move(C('a4'))
        self.assertFalse(result)

    def test_invalid_samepos(self):
        board = StubBoard()

        queen = self.get_queen(board, WHITE, C('e4'))
        result = queen.is_valid_move(C('e4'))
        self.assertFalse(result)
    # -------------------------------------------------------------------------


    # VALID MOVES -------------------------------------------------------------
    def test_valid_topright(self):
        board = StubBoard()

        queen = self.get_queen(board, WHITE, C('e4'))
        result = queen.is_valid_move(C('h7'))
        self.assertTrue(result)

    def test_valid_topleft(self):
        board = StubBoard()

        queen = self.get_queen(board, WHITE, C('e4'))
        result = queen.is_valid_move(C('a8'))
        self.assertTrue(result)

    def test_valid_bottomleft(self):
        board = StubBoard()

        queen = self.get_queen(board, WHITE, C('e4'))
        result = queen.is_valid_move(C('b1'))
        self.assertTrue(result)

    def test_valid_bottomright(self):
        board = StubBoard()

        queen = self.get_queen(board, WHITE, C('e4'))
        result = queen.is_valid_move(C('h1'))
        self.assertTrue(result)

    def test_valid_topright2(self):
        board = StubBoard()
        board[C('c2')] = StubPiece(board, WHITE, C('c2'))
        board[C('e2')] = StubPiece(board, WHITE, C('e2'))

        queen = self.get_queen(board, WHITE, C('c1'))
        result = queen.is_valid_move(C('f4'))
        self.assertTrue(result)
    # -------------------------------------------------------------------------

    # INVALID MOVES -----------------------------------------------------------
    def test_invalid_obstructed_topright(self):
        board = StubBoard()
        board[C('g6')] = StubPiece(board, WHITE, C('g6'))

        queen = self.get_queen(board, BLACK, C('e4'))
        result = queen.is_valid_move(C('h7'))
        self.assertFalse(result)

    def test_invalid_obstructed_topleft(self):
        board = StubBoard()
        board[C('b7')] = StubPiece(board, WHITE, C('b7'))

        queen = self.get_queen(board, BLACK, C('e4'))
        result = queen.is_valid_move(C('a8'))
        self.assertFalse(result)

    def test_invalid_obstructed_bottomleft(self):
        board = StubBoard()
        board[C('c2')] = StubPiece(board, WHITE, C('c2'))

        queen = self.get_queen(board, BLACK, C('e4'))
        result = queen.is_valid_move(C('b1'))
        self.assertFalse(result)

    def test_invalid_obstructed_bottomright(self):
        board = StubBoard()
        board[C('g2')] = StubPiece(board, WHITE, C('g2'))

        queen = self.get_queen(board, BLACK, C('e4'))
        result = queen.is_valid_move(C('h1'))
        self.assertFalse(result)
    # -------------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()