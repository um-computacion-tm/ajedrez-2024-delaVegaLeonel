import unittest
from game.king import King
from game.chess import Chess

class TestKing(unittest.TestCase):
    def test_king_moves(self):
        chess = Chess()
        king = King()
        self.assertEqual(king.move(chess), "e1")
        self.assertEqual(king.move(chess), "f1")
        self.assertEqual(king.move(chess), "g1")
        self.assertEqual(king.move(chess), "h1")
        self.assertEqual(king.move(chess), "e8")
        self.assertEqual(king.move(chess), "f8")
        self.assertEqual(king.move(chess), "g8")
        self.assertEqual(king.move(chess), "h8")