import unittest
from game.rook import Rook
from game.board import Board

class TestRook(unittest.TestCase):
    def setUp(self):
        self.__rook__ = Rook("WHITE")
        self.__board__ = Board()

    def test_rook_move(self):
        executing_move = [1, 7]
        self.__board__.place_piece(self.__rook__, (1, 7))
        self.assertEqual(self.__board__.get_piece_at((1, 7)), self.__rook__)

    def test_rook_not_move(self):
        self.__board__.place_piece(self.__rook__, (1, 7))
        self.assertNotEqual(self.__board__.get_piece_at((1, 8)), self.__rook__)


def test_rook_possible_movements(self):
        possible_movements = self.__rook__.possible_movements()
        self.assertIn((1, 7), possible_movements)
