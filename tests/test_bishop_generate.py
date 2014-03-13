import unittest
from .helpers import StubBoard, StubPiece, C, WHITE, BLACK

class TestBishopGenerate(unittest.TestCase):
    def get_bishop(self, board, team, position):
        from chess.models import Bishop
        return Bishop(board, team, position)

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

    def test_generate_topright(self):
        board = StubBoard()
        board[C('h7')] = StubPiece(board, BLACK, C('h7'))
        bishop = self.get_bishop(board, WHITE, C('e4'))
        results = bishop.generate()
        expected = [C('f5'), C('g6'), C('h7')]

        correct = self.compare_list(expected, results)
        self.assertTrue(all(correct))

    def test_generate_topleft(self):
        board = StubBoard()
        board[C('c6')] = StubPiece(board, WHITE, C('c6'))
        bishop = self.get_bishop(board, WHITE, C('e4'))
        results = bishop.generate()
        expected = [C('d5')]

        correct = self.compare_list(expected, results)
        self.assertTrue(all(correct))

        expected = [C('c6')]
        correct = self.compare_list(expected, results)
        self.assertFalse(any(correct))

    def test_generate_bottomleft(self):
        board = StubBoard()
        board[C('c2')] = StubPiece(board, BLACK, C('c2'))
        bishop = self.get_bishop(board, WHITE, C('e4'))
        results = bishop.generate()
        expected = [C('d3'), C('c2')]

        correct = self.compare_list(expected, results)
        self.assertTrue(all(correct))

        expected = [C('b1')]
        correct = self.compare_list(expected, results)
        self.assertFalse(any(correct))

    def test_generate_bottomright(self):
        board = StubBoard()
        bishop = self.get_bishop(board, WHITE, C('e4'))
        results = bishop.generate()
        expected = [C('f3'), C('g2'), C('h1')]

        correct = self.compare_list(expected, results)
        self.assertTrue(all(correct))

    def test_generate_amount(self):
        board = StubBoard()
        bishop = self.get_bishop(board, WHITE, C('e4'))
        results = bishop.generate()

        self.assertEqual(len(results), 13)


        board = StubBoard()
        board[C('c6')] = StubPiece(board, WHITE, C('c6'))
        bishop = self.get_bishop(board, WHITE, C('e4'))
        results = bishop.generate()

        self.assertEqual(len(results), 10)


if __name__ == '__main__':
    unittest.main()