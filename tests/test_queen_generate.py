import unittest
from .helpers import StubBoard, StubPiece, C, WHITE, BLACK

class TestQueenGenerate(unittest.TestCase):
    def get_queen(self, board, team, position):
        from chess.models import Queen
        return Queen(board, team, position)

    def compare_list(self, expected, results):
        compared = []

        for e in expected:
            for r in results:
                if e[0] == r[0] and e[1] == r[1]:
                    compared.append(True)
                    break
            else:
                compared.append(False)

        return compared

    def test_generate_horizontal_right(self):
        board = StubBoard()
        board[C('g4')] = StubPiece(board, BLACK, None)
        board[C('e7')] = StubPiece(board, WHITE, None)
        board[C('a4')] = StubPiece(board, WHITE, None)
        board[C('e1')] = StubPiece(board, BLACK, None)

        queen = self.get_queen(board, WHITE, C('e4'))
        results = queen.generate()
        expected = [C('f4'), C('g4')]

        correct = self.compare_list(expected, results)
        self.assertTrue(all(correct))

    def test_generate_horizontal_left(self):
        board = StubBoard()
        board[C('g4')] = StubPiece(board, BLACK, None)
        board[C('e7')] = StubPiece(board, WHITE, None)
        board[C('a4')] = StubPiece(board, BLACK, None)
        board[C('e1')] = StubPiece(board, BLACK, None)

        queen = self.get_queen(board, WHITE, C('e4'))
        results = queen.generate()
        expected = [C('d4'), C('c4'), C('b4'), C('a4')]

        correct = self.compare_list(expected, results)
        self.assertTrue(all(correct))

    def test_generate_vertical_top(self):
        board = StubBoard()
        board[C('g4')] = StubPiece(board, BLACK, None)
        board[C('e7')] = StubPiece(board, WHITE, None)
        board[C('a4')] = StubPiece(board, WHITE, None)
        board[C('e1')] = StubPiece(board, BLACK, None)

        queen = self.get_queen(board, WHITE, C('e4'))
        results = queen.generate()
        expected = [C('e5'), C('e6')]

        correct = self.compare_list(expected, results)
        self.assertTrue(all(correct))

    def test_generate_vertical_bottom(self):
        board = StubBoard()
        board[C('g4')] = StubPiece(board, BLACK, None)
        board[C('e7')] = StubPiece(board, WHITE, None)
        board[C('a4')] = StubPiece(board, WHITE, None)
        board[C('e1')] = StubPiece(board, BLACK, None)

        queen = self.get_queen(board, WHITE, C('e4'))
        results = queen.generate()
        expected = [C('e3'), C('e2'), C('e1')]

        correct = self.compare_list(expected, results)
        self.assertTrue(all(correct))
        
    def test_generate_topright(self):
        board = StubBoard()
        board[C('h7')] = StubPiece(board, BLACK, C('h7'))
        queen = self.get_queen(board, WHITE, C('e4'))
        results = queen.generate()
        expected = [C('f5'), C('g6'), C('h7')]

        correct = self.compare_list(expected, results)
        self.assertTrue(all(correct))

    def test_generate_topleft(self):
        board = StubBoard()
        board[C('c6')] = StubPiece(board, WHITE, C('c6'))
        queen = self.get_queen(board, WHITE, C('e4'))
        results = queen.generate()
        expected = [C('d5')]

        correct = self.compare_list(expected, results)
        self.assertTrue(all(correct))

        expected = [C('c6')]
        correct = self.compare_list(expected, results)
        self.assertFalse(any(correct))

    def test_generate_bottomleft(self):
        board = StubBoard()
        board[C('c2')] = StubPiece(board, BLACK, C('c2'))
        queen = self.get_queen(board, WHITE, C('e4'))
        results = queen.generate()
        expected = [C('d3'), C('c2')]

        correct = self.compare_list(expected, results)
        self.assertTrue(all(correct))

        expected = [C('b1')]
        correct = self.compare_list(expected, results)
        self.assertFalse(any(correct))

    def test_generate_bottomright(self):
        board = StubBoard()
        queen = self.get_queen(board, WHITE, C('e4'))
        results = queen.generate()
        expected = [C('f3'), C('g2'), C('h1')]

        correct = self.compare_list(expected, results)
        self.assertTrue(all(correct))

if __name__ == '__main__':
    unittest.main()