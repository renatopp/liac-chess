import unittest
from .helpers import StubBoard, StubPiece, C, WHITE, BLACK

class TestRookGenerate(unittest.TestCase):
    def get_rook(self, board, team, position):
        from chess.models import Rook
        return Rook(board, team, position)

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

        rook = self.get_rook(board, WHITE, C('e4'))
        results = rook.generate()
        expected = [C('f4'), C('g4')]

        correct = self.compare_list(expected, results)
        self.assertTrue(all(correct))

    def test_generate_horizontal_left(self):
        board = StubBoard()
        board[C('g4')] = StubPiece(board, BLACK, None)
        board[C('e7')] = StubPiece(board, WHITE, None)
        board[C('a4')] = StubPiece(board, BLACK, None)
        board[C('e1')] = StubPiece(board, BLACK, None)

        rook = self.get_rook(board, WHITE, C('e4'))
        results = rook.generate()
        expected = [C('d4'), C('c4'), C('b4'), C('a4')]

        correct = self.compare_list(expected, results)
        self.assertTrue(all(correct))

    def test_generate_vertical_top(self):
        board = StubBoard()
        board[C('g4')] = StubPiece(board, BLACK, None)
        board[C('e7')] = StubPiece(board, WHITE, None)
        board[C('a4')] = StubPiece(board, WHITE, None)
        board[C('e1')] = StubPiece(board, BLACK, None)

        rook = self.get_rook(board, WHITE, C('e4'))
        results = rook.generate()
        expected = [C('e5'), C('e6')]

        correct = self.compare_list(expected, results)
        self.assertTrue(all(correct))

    def test_generate_vertical_bottom(self):
        board = StubBoard()
        board[C('g4')] = StubPiece(board, BLACK, None)
        board[C('e7')] = StubPiece(board, WHITE, None)
        board[C('a4')] = StubPiece(board, WHITE, None)
        board[C('e1')] = StubPiece(board, BLACK, None)

        rook = self.get_rook(board, WHITE, C('e4'))
        results = rook.generate()
        expected = [C('e3'), C('e2'), C('e1')]

        correct = self.compare_list(expected, results)
        print correct
        print results
        print expected
        self.assertTrue(all(correct))

if __name__ == '__main__':
    unittest.main()