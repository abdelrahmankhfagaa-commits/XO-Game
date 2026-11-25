
import unittest

from game.player import Player
from game.human_player import HumanPlayer


class TestPlayer(unittest.TestCase):

    def test_player_is_abstract(self):
        with self.assertRaises(TypeError):
            Player("Player", "X")

    def test_empty_name_is_rejected(self):
        with self.assertRaises(ValueError):
            HumanPlayer("", "X")

    def test_invalid_symbol_is_rejected(self):
        with self.assertRaises(ValueError):
            HumanPlayer("Player", "A")

    def test_name_and_symbol(self):
        player = HumanPlayer("Player 1", "X")

        self.assertEqual(player.name, "Player 1")
        self.assertEqual(player.symbol, "X")

    def test_human_get_valid_move(self):
        from game.board import Board

        player = HumanPlayer("Player 1", "X")
        board = Board()

        self.assertEqual(player.get_move(board, 4), 4)

    def test_human_rejects_occupied_cell(self):
        from game.board import Board

        player = HumanPlayer("Player 1", "X")
        board = Board()
        board.make_move(4, "O")

        with self.assertRaises(ValueError):
            player.get_move(board, 4)

    def test_human_requires_position(self):
        from game.board import Board

        player = HumanPlayer("Player 1", "X")
        board = Board()

        with self.assertRaises(ValueError):
            player.get_move(board)


if __name__ == "__main__":
    unittest.main()
