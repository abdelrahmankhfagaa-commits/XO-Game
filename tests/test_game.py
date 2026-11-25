
import unittest

from game.game import Game
from game.human_player import HumanPlayer
from game.scoreboard import Scoreboard


class TestGame(unittest.TestCase):

    def setUp(self):
        self.player1 = HumanPlayer("Player 1", "X")
        self.player2 = HumanPlayer("Player 2", "O")
        self.scoreboard = Scoreboard()

        self.game = Game(
            [self.player1, self.player2],
            self.scoreboard
        )

    def test_x_starts_first(self):
        self.assertIs(self.game.current_player, self.player1)

    def test_turn_switching(self):
        self.game.play_turn(0)

        self.assertIs(self.game.current_player, self.player2)

    def test_winner_and_score(self):
        for move in [0, 3, 1, 4, 2]:
            self.game.play_turn(move)

        self.assertTrue(self.game.game_over)
        self.assertIs(self.game.winner, self.player1)
        self.assertEqual(self.scoreboard.x_wins, 1)

    def test_draw_and_score(self):
        moves = [0, 1, 2, 4, 3, 5, 7, 6, 8]

        for move in moves:
            self.game.play_turn(move)

        self.assertTrue(self.game.game_over)
        self.assertIsNone(self.game.winner)
        self.assertEqual(self.scoreboard.draws, 1)

    def test_restart_preserves_score(self):
        for move in [0, 3, 1, 4, 2]:
            self.game.play_turn(move)

        self.game.start_new_round()

        self.assertFalse(self.game.game_over)
        self.assertIsNone(self.game.winner)
        self.assertEqual(self.scoreboard.x_wins, 1)
        self.assertIs(self.game.current_player, self.player1)

    def test_cannot_play_after_game_over(self):
        for move in [0, 3, 1, 4, 2]:
            self.game.play_turn(move)

        with self.assertRaises(RuntimeError):
            self.game.play_turn(8)

    def test_invalid_move_does_not_switch_turn(self):
        self.game.play_turn(0)

        with self.assertRaises(ValueError):
            self.game.play_turn(0)

        self.assertIs(self.game.current_player, self.player2)

    def test_duplicate_symbols_are_rejected(self):
        duplicate_player = HumanPlayer("Player 3", "X")

        with self.assertRaises(ValueError):
            Game(
                [self.player1, duplicate_player],
                self.scoreboard
            )


if __name__ == "__main__":
    unittest.main()
