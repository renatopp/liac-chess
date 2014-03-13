import unittest
from .helpers import StubBoard, StubPiece, C, WHITE, BLACK

class TestRookMovement(unittest.TestCase):
    def get_rook(self, board, team, position):
        from chess.models import Rook
        return Rook(board, team, position)

    # VALID MOVES -------------------------------------------------------------
    def test_valid_vertical(self):
        board = StubBoard()

        # Top
        rook = self.get_rook(board, WHITE, C('e4'))
        result = rook.is_valid_move(C('e8'))
        self.assertTrue(result)

        # Bottom
        rook = self.get_rook(board, WHITE, C('e4'))
        result = rook.is_valid_move(C('e1'))
        self.assertTrue(result)

    def test_valid_horizontal(self):
        board = StubBoard()

        # Right
        rook = self.get_rook(board, WHITE, C('e4'))
        result = rook.is_valid_move(C('h4'))
        self.assertTrue(result)

        # Left
        rook = self.get_rook(board, WHITE, C('e4'))
        result = rook.is_valid_move(C('a4'))
        self.assertTrue(result)
    # -------------------------------------------------------------------------

    # INVALID MOVES -----------------------------------------------------------
    def test_invalid_diagonal(self):
        board = StubBoard()

        rook = self.get_rook(board, WHITE, C('e4'))
        result = rook.is_valid_move(C('d5'))
        self.assertFalse(result)
        
        rook = self.get_rook(board, WHITE, C('e4'))
        result = rook.is_valid_move(C('f5'))
        self.assertFalse(result)

        rook = self.get_rook(board, WHITE, C('e4'))
        result = rook.is_valid_move(C('d3'))
        self.assertFalse(result)

        rook = self.get_rook(board, WHITE, C('e4'))
        result = rook.is_valid_move(C('f3'))
        self.assertFalse(result)      

    def test_invalid_obstructedvertical(self):
        board = StubBoard()
        board[C('e7')] = StubPiece(board, WHITE, C('e7'))
        board[C('e2')] = StubPiece(board, WHITE, C('e2'))

        # Top
        rook = self.get_rook(board, BLACK, C('e4'))
        result = rook.is_valid_move(C('e8'))
        self.assertFalse(result)

        # Bottom
        rook = self.get_rook(board, BLACK, C('e4'))
        result = rook.is_valid_move(C('e1'))
        self.assertFalse(result)

    def test_invalid_obstructedhorizontal(self):
        board = StubBoard()
        board[C('g4')] = StubPiece(board, WHITE, C('g4'))
        board[C('b4')] = StubPiece(board, WHITE, C('b4'))

        # Right
        rook = self.get_rook(board, WHITE, C('e4'))
        result = rook.is_valid_move(C('h4'))
        self.assertFalse(result)

        # Left
        rook = self.get_rook(board, WHITE, C('e4'))
        result = rook.is_valid_move(C('a4'))
        self.assertFalse(result)

    def test_invalid_samepos(self):
        board = StubBoard()

        rook = self.get_rook(board, WHITE, C('e4'))
        result = rook.is_valid_move(C('e4'))
        self.assertFalse(result)

    # -------------------------------------------------------------------------

if __name__ == '__main__':
    unittest.main()