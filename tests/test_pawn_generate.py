import unittest
from .helpers import StubBoard, StubPiece, C, WHITE, BLACK

class TestPawnGenerate(unittest.TestCase):
    def get_pawn(self, board, team, position):
        from chess.models import Pawn
        return Pawn(board, team, position)

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

    def test_generate_simple(self):
        board = StubBoard()
        pawn = self.get_pawn(board, WHITE, C('d4'))
        pawn.move_to(C('d5'))
        
        results = pawn.generate()
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][0], C('d6')[0])
        self.assertEqual(results[0][1], C('d6')[1])


        board = StubBoard()
        pawn = self.get_pawn(board, BLACK, C('f6'))
        pawn.move_to(C('f5'))
        
        results = pawn.generate()
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0][0], C('f4')[0])
        self.assertEqual(results[0][1], C('f4')[1])

    def test_generate_double(self):
        board = StubBoard()
        pawn = self.get_pawn(board, WHITE, C('e2'))
        
        results = pawn.generate()
        expected = [C('e3'), C('e4')]

        self.assertEqual(len(results), 2)
        correct = self.compare_list(expected, results)
        self.assertTrue(all(correct))


        board = StubBoard()
        pawn = self.get_pawn(board, BLACK, C('e7'))
        
        results = pawn.generate()
        expected = [C('e6'), C('e5')]

        self.assertEqual(len(results), 2)
        correct = self.compare_list(expected, results)
        self.assertTrue(all(correct))

    def test_generate_capture(self):
        board = StubBoard()
        board[C('e3')] = StubPiece(board, BLACK, C('e3'))
        board[C('c3')] = StubPiece(board, BLACK, C('c3'))
        pawn = self.get_pawn(board, WHITE, C('d2'))
        
        results = pawn.generate()
        expected = [C('d3'), C('d4'), C('e3'), C('c3')]

        correct = self.compare_list(expected, results)
        self.assertEqual(len(expected), len(results))
        self.assertTrue(all(correct), correct)


        board = StubBoard()
        board[C('e6')] = StubPiece(board, WHITE, C('e6'))
        board[C('c6')] = StubPiece(board, WHITE, C('c6'))
        pawn = self.get_pawn(board, BLACK, C('d7'))
        
        results = pawn.generate()
        expected = [C('d6'), C('d5'), C('e6'), C('c6')]

        correct = self.compare_list(expected, results)
        self.assertEqual(len(expected), len(results))
        self.assertTrue(all(correct), correct)

    def test_generate_nocapture(self):
        board = StubBoard()
        board[C('e3')] = StubPiece(board, BLACK, C('e3'))
        board[C('c3')] = StubPiece(board, WHITE, C('c3'))
        pawn = self.get_pawn(board, WHITE, C('d2'))
        
        results = pawn.generate()
        expected = [C('d3'), C('d4'), C('e3')]

        correct = self.compare_list(expected, results)
        self.assertEqual(len(expected), len(results))
        self.assertTrue(all(correct), correct)


        board = StubBoard()
        board[C('e6')] = StubPiece(board, WHITE, C('e6'))
        board[C('c6')] = StubPiece(board, BLACK, C('c6'))
        pawn = self.get_pawn(board, BLACK, C('d7'))
        
        results = pawn.generate()
        expected = [C('d6'), C('d5'), C('e6')]

        correct = self.compare_list(expected, results)
        self.assertEqual(len(expected), len(results))
        self.assertTrue(all(correct), correct)

    def test_generate_blocked(self):
        board = StubBoard()
        board[C('e3')] = StubPiece(board, BLACK, C('e3'))
        pawn = self.get_pawn(board, WHITE, C('e2'))
        
        results = pawn.generate()
        self.assertEqual(len(results), 0)


        board = StubBoard()
        board[C('e6')] = StubPiece(board, WHITE, C('e6'))
        pawn = self.get_pawn(board, BLACK, C('e7'))
        
        results = pawn.generate()
        self.assertEqual(len(results), 0)

    def test_generate_blocked2(self):
        board = StubBoard()
        board[C('e4')] = StubPiece(board, BLACK, C('e4'))
        pawn = self.get_pawn(board, WHITE, C('e2'))
        
        results = pawn.generate()
        expected = [C('e3')]

        correct = self.compare_list(expected, results)
        self.assertEqual(len(expected), len(results))
        self.assertTrue(all(correct), correct)


        board = StubBoard()
        board[C('e5')] = StubPiece(board, WHITE, C('e5'))
        pawn = self.get_pawn(board, BLACK, C('e7'))
        
        results = pawn.generate()
        expected = [C('e6')]

        correct = self.compare_list(expected, results)
        self.assertEqual(len(expected), len(results))
        self.assertTrue(all(correct), correct)

    def test_generate_enpassant(self):
        board = StubBoard()
        board.enpassant = C('c6')
        board[C('c5')] = StubPiece(board, BLACK, C('c5'))

        pawn = self.get_pawn(board, WHITE, C('b4'))
        pawn.move_to(C('b5'))

        results = pawn.generate()
        expected = [C('c6'), C('b6')]

        correct = self.compare_list(expected, results)
        self.assertEqual(len(expected), len(results))
        self.assertTrue(all(correct), correct)


        board = StubBoard()
        board.enpassant = C('e3')
        board[C('e4')] = StubPiece(board, WHITE, C('e4'))

        pawn = self.get_pawn(board, BLACK, C('d5'))
        pawn.move_to(C('d4'))

        results = pawn.generate()
        expected = [C('d3'), C('e3')]

        correct = self.compare_list(expected, results)
        self.assertEqual(len(expected), len(results))
        self.assertTrue(all(correct), correct)

    def test_generate_no_enpassant(self):
        board = StubBoard()
        board.enpassant = C('g6')
        board[C('g5')] = StubPiece(board, BLACK, C('g5'))

        pawn = self.get_pawn(board, WHITE, C('b4'))
        pawn.move_to(C('b5'))

        results = pawn.generate()
        expected = [C('b6')]

        correct = self.compare_list(expected, results)
        self.assertEqual(len(expected), len(results))
        self.assertTrue(all(correct), correct)


        board = StubBoard()
        board.enpassant = C('h3')
        board[C('h4')] = StubPiece(board, WHITE, C('h4'))

        pawn = self.get_pawn(board, BLACK, C('d5'))
        pawn.move_to(C('d4'))

        results = pawn.generate()
        expected = [C('d3')]

        correct = self.compare_list(expected, results)
        self.assertEqual(len(expected), len(results))
        self.assertTrue(all(correct), correct)
        
if __name__ == '__main__':
    unittest.main()