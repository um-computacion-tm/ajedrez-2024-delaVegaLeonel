import unittest
from game.rook import Rook

def setUp(self):
    self.__rook__ = Rook("WHITE")  

def test_rook_possible_movements(self):
        possible_movements = self.__rook__.possible_movements()
        self.assertIn((1, 7), possible_movements)
