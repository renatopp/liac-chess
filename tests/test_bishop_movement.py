import unittest
from .helpers import StubBoard, StubPiece, C, WHITE, BLACK

class TestBishopMovement(unittest.TestCase):
    def get_bishop(self, board, team, position):
        from chess.models import Bishop
        return Bishop(board, team, position)

    # VALID MOVES -------------------------------------------------------------
    def test_valid_topright(self):
        board = StubBoard()

        bishop = self.get_bishop(board, WHITE, C('e4'))
        result = bishop.is_valid_move(C('h7'))
        self.assertTrue(result)

    def test_valid_topleft(self):
        board = StubBoard()

        bishop = self.get_bishop(board, WHITE, C('e4'))
        result = bishop.is_valid_move(C('a8'))
        self.assertTrue(result)

    def test_valid_bottomleft(self):
        board = StubBoard()

        bishop = self.get_bishop(board, WHITE, C('e4'))
        result = bishop.is_valid_move(C('b1'))
        self.assertTrue(result)

    def test_valid_bottomright(self):
        board = StubBoard()

        bishop = self.get_bishop(board, WHITE, C('e4'))
        result = bishop.is_valid_move(C('h1'))
        self.assertTrue(result)

    def test_valid_topright2(self):
        board = StubBoard()
        board[C('c2')] = StubPiece(board, WHITE, C('c2'))
        board[C('e2')] = StubPiece(board, WHITE, C('e2'))

        bishop = self.get_bishop(board, WHITE, C('c1'))
        result = bishop.is_valid_move(C('f4'))
        self.assertTrue(result)
    # -------------------------------------------------------------------------

    # INVALID MOVES -----------------------------------------------------------
    def test_invalid_horizontal(self):
        board = StubBoard()

        bishop = self.get_bishop(board, WHITE, C('e4'))
        result = bishop.is_valid_move(C('d4'))
        self.assertFalse(result)
        
        bishop = self.get_bishop(board, WHITE, C('e4'))
        result = bishop.is_valid_move(C('c4'))
        self.assertFalse(result)

    def test_invalid_vertical(self):
        board = StubBoard()

        bishop = self.get_bishop(board, WHITE, C('e4'))
        result = bishop.is_valid_move(C('e3'))
        self.assertFalse(result)

        bishop = self.get_bishop(board, WHITE, C('e4'))
        result = bishop.is_valid_move(C('e5'))
        self.assertFalse(result)     

    def test_invalid_obstructed_topright(self):
        board = StubBoard()
        board[C('g6')] = StubPiece(board, WHITE, C('g6'))

        bishop = self.get_bishop(board, BLACK, C('e4'))
        result = bishop.is_valid_move(C('h7'))
        self.assertFalse(result)

    def test_invalid_obstructed_topleft(self):
        board = StubBoard()
        board[C('b7')] = StubPiece(board, WHITE, C('b7'))

        bishop = self.get_bishop(board, BLACK, C('e4'))
        result = bishop.is_valid_move(C('a8'))
        self.assertFalse(result)

    def test_invalid_obstructed_bottomleft(self):
        board = StubBoard()
        board[C('c2')] = StubPiece(board, WHITE, C('c2'))

        bishop = self.get_bishop(board, BLACK, C('e4'))
        result = bishop.is_valid_move(C('b1'))
        self.assertFalse(result)

    def test_invalid_obstructed_bottomright(self):
        board = StubBoard()
        board[C('g2')] = StubPiece(board, WHITE, C('g2'))

        bishop = self.get_bishop(board, BLACK, C('e4'))
        result = bishop.is_valid_move(C('h1'))
        self.assertFalse(result)

    def test_invalid_samepos(self):
        board = StubBoard()

        bishop = self.get_bishop(board, BLACK, C('e4'))
        result = bishop.is_valid_move(C('e4'))
        self.assertFalse(result)
    # -------------------------------------------------------------------------


if __name__ == '__main__':
    unittest.main()