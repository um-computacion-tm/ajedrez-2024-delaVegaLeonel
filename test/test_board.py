import unittest
from game.rook import Rook
from game.board import Board

class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_initial_rook_positions(self):
        # torres negras
        self.assertIsInstance(self.board.get_piece(0, 0), Rook)
        self.assertEqual(self.board.get_piece(0, 0).color, "BLACK")
        
        self.assertIsInstance(self.board.get_piece(0, 7), Rook)
        self.assertEqual(self.board.get_piece(0, 7).color, "BLACK")
        
        # torres blancas
        self.assertIsInstance(self.board.get_piece(7, 0), Rook)
        self.assertEqual(self.board.get_piece(7, 0).color, "WHITE")
        
        self.assertIsInstance(self.board.get_piece(7, 7), Rook)
        self.assertEqual(self.board.get_piece(7, 7).color, "WHITE")
        
    def test_empty_squares(self):
        # Comprobamos que el resto del tablero está vacío
        for row in range(8):
            for col in range(8):
                if not ((row == 0 and (col == 0 or col == 7)) or 
                        (row == 7 and (col == 0 or col == 7))):
                    self.assertIsNone(self.board.get_piece(row, col))

if __name__ == '__main__':
    unittest.main()