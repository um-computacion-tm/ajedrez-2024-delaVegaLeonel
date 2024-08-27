import unittest
from game.queen import Queen
from game.board import Board

class TestQueen(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.queen = Queen(self.board)

    def test_get_move_Queen(self):
        self.assertEqual(self.queen.get_move_Queen(self.board, 1, 1), [(2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2)])

    def test_posibles_moves(self):
        self.assertEqual(self.queen.posibles_moves(1, 1), [(2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2)])

if __name__ == '__main__':
    unittest.main() 