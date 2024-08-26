import unittest
from game.pawn import Pawn
from game.chess import Chess

class TestPawn(unittest.TestCase):
    def test_str(self):
        pawn = Pawn("WHITE")
        self.assertEqual(str(pawn), "♙")
        pawn = Pawn("BLACK")
        self.assertEqual(str(pawn), "♟")