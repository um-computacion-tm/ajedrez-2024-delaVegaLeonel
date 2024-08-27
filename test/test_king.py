import unittest
from game.king import King
from game.chess import Chess
from game.piece import Piece
from game.board import Board
"""""
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
        self.assertEqual(king.move(chess), "h8")"""""

class TestKing(unittest.TestCase):

    def setUp(self):
        self.board = Board()
        self.white_king = King("white", self.board)
        self.black_king = King("black", self.board)

    def test_white_king_symbol(self):
        self.assertEqual(str(self.white_king), "♔")

    def test_black_king_symbol(self):
        self.assertEqual(str(self.black_king), "♚")

    def test_get_move_king_in_center(self):
        self.board.place_piece(self.white_king, 4, 4)
        expected_moves = [(3, 3), (3, 4), (3, 5), (4, 3), (4, 5), (5, 3), (5, 4), (5, 5)]
        self.assertEqual(set(self.white_king.get_move_king(self.board, 4, 4)), set(expected_moves))

    def test_get_move_king_on_edge(self):
        self.board.place_piece(self.black_king, 1, 4)
        expected_moves = [(1, 3), (1, 5), (2, 3), (2, 4), (2, 5)]
        self.assertEqual(set(self.black_king.get_move_king(self.board, 1, 4)), set(expected_moves))

    def test_get_move_king_on_corner(self):
        self.board.place_piece(self.white_king, 1, 1)
        expected_moves = [(1, 2), (2, 1), (2, 2)]
        self.assertEqual(set(self.white_king.get_move_king(self.board, 1, 1)), set(expected_moves))

    def test_king_blocked_by_pieces(self):
        self.board.place_piece(self.white_king, 4, 4)
        blocking_piece_1 = Piece("white", self.board)
        blocking_piece_2 = Piece("white", self.board)
        self.board.place_piece(blocking_piece_1, 3, 4)
        self.board.place_piece(blocking_piece_2, 5, 4)
        expected_moves = [(3, 3), (3, 5), (4, 3), (4, 5), (5, 3), (5, 5)]
        self.assertEqual(set(self.white_king.get_move_king(self.board, 4, 4)), set(expected_moves))

    def test_posibles_moves(self): 
        self.board.place_piece(self.white_king, 4, 4)
        expected_moves = self.white_king.get_move_king(self.board, 4, 4)
        self.assertEqual(set(self.white_king.posibles_moves(4, 4)), set(expected_moves))

    def test_king_not_on_board(self):  
        self.assertEqual(self.white_king.posibles_moves(4, 4), [])

if __name__ == "__main__":
    unittest.main()

