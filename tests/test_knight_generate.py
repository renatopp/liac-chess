import unittest
from .helpers import StubBoard, StubPiece, C, WHITE, BLACK

class TestKnightMovement(unittest.TestCase):
    def get_knight(self, board, team, position):
        from chess.models import Knight
        return Knight(board, team, position)

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

    def test_generate_empty(self):
        board = StubBoard()
        knight = self.get_knight(board, WHITE, C('e4'))
        results = knight.generate()
        expected = [C('f6'), C('g5'), 
                    C('d6'), C('c5'),
                    C('c3'), C('d2'),
                    C('g3'), C('f2')]

        correct = self.compare_list(expected, results)
        self.assertTrue(all(correct))
        self.assertEqual(len(results), len(expected))

    def test_generate_obstacle(self):
        board = StubBoard()
        board[C('f6')] = StubPiece(board, BLACK, C('f6'))
        board[C('g3')] = StubPiece(board, WHITE, C('g3'))
        knight = self.get_knight(board, WHITE, C('e4'))
        results = knight.generate()
        expected = [C('f6'), C('g5'), 
                    C('d6'), C('c5'),
                    C('c3'), C('d2'),
                             C('f2')]

        correct = self.compare_list(expected, results)
        print correct
        self.assertTrue(all(correct))
        self.assertEqual(len(results), len(expected))

    def test_generate_border(self):
        board = StubBoard()
        knight = self.get_knight(board, WHITE, C('h8'))
        results = knight.generate()
        expected = [C('g6'), C('f7')]

        correct = self.compare_list(expected, results)
        print correct
        self.assertTrue(all(correct))
        self.assertEqual(len(results), len(expected))



if __name__ == '__main__':
    unittest.main()