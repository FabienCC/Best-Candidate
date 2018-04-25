import unittest

from best_candidate import get_pieces_for, Piece

class Test(unittest.TestCase):
    def test_1(self):
        OBJECT_DIMENSION = Piece(10, 10, 10) # (X, Y, Z)

        LIBRARY = [
            Piece(10, 1, 10),
        ] * 10

        solution = get_pieces_for(OBJECT_DIMENSION, LIBRARY)
        self.assertEqual(solution, LIBRARY)

    def test_2(self):
        OBJECT_DIMENSION = Piece(10, 10, 10) # (X, Y, Z)

        LIBRARY = [Piece(10, 1, 10)] * 10 + [Piece(10, 5, 10)]

        solution = get_pieces_for(OBJECT_DIMENSION, LIBRARY)
        self.assertEqual(solution, [LIBRARY[-1]] + LIBRARY[:5])

    def test_3(self):
        OBJECT_DIMENSION = Piece(10, 10, 10) # (X, Y, Z)

        LIBRARY = [Piece(9.99, 1, 10)] * 10 + [Piece(10, 5, 10)]

        self.assertRaises(Exception, get_pieces_for, OBJECT_DIMENSION, LIBRARY)

if __name__ == '__main__':
    unittest.main()
