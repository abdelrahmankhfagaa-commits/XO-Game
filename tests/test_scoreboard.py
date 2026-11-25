
import unittest

from game.scoreboard import Scoreboard


class TestScoreboard(unittest.TestCase):

    def setUp(self):
        self.scoreboard = Scoreboard()

    def test_scores_start_at_zero(self):
        self.assertEqual(self.scoreboard.x_wins, 0)
        self.assertEqual(self.scoreboard.o_wins, 0)
        self.assertEqual(self.scoreboard.draws, 0)

    def test_record_x_win(self):
        self.scoreboard.record_win("X")
        self.assertEqual(self.scoreboard.x_wins, 1)

    def test_record_o_win(self):
        self.scoreboard.record_win("O")
        self.assertEqual(self.scoreboard.o_wins, 1)

    def test_record_draw(self):
        self.scoreboard.record_draw()
        self.assertEqual(self.scoreboard.draws, 1)

    def test_reset_scores(self):
        self.scoreboard.record_win("X")
        self.scoreboard.record_win("O")
        self.scoreboard.record_draw()

        self.scoreboard.reset_scores()

        self.assertEqual(self.scoreboard.x_wins, 0)
        self.assertEqual(self.scoreboard.o_wins, 0)
        self.assertEqual(self.scoreboard.draws, 0)

    def test_invalid_winner_symbol(self):
        with self.assertRaises(ValueError):
            self.scoreboard.record_win("A")


if __name__ == "__main__":
    unittest.main()
