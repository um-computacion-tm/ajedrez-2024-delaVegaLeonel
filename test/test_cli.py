import unittest
from game.chess import Chess
from game.cli import play 

class TestCli(unittest.TestCase):
    @patch( #este patch controla lo que hace
        "builtins.input",
        side_effect=["1"."1","2","2"], 

    )

    @patch("builtins.print")
    @patch.objets(Chess,"move")
    def test_happy_patch(
        self,
        mock_chess_move,
        mock_print,
        mock_input
    ):
        chess=Chess()
        play(chess)
        self.assertEqual(mock_input.call_count,4)
        self.assertEqual(mock_print.call_count,2)
        self.assertEqual(mock_chess_move.call_count,1)

    @patch("builtins.print")
    @patch.objets(Chess,"move")
    def test_more_not_happy_patch(
            self, 
            mock_print,
            mock_input    
        ):

        chess=Chess()
        play(chess)
        self.assertEqual(mock_input.call_count,4)
        self.assertEqual(mock_print.call_count,2)