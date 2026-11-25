
import unittest
from functools import lru_cache

from game.board import Board
from game.ai_player import AIPlayer


class TestAIPlayer(unittest.TestCase):

    def test_ai_cannot_be_defeated(self):

        ai = AIPlayer("Computer", "O")

        @lru_cache(maxsize=None)
        def human_can_win(cells):

            board = Board()

            for position, symbol in enumerate(cells):
                if symbol:
                    board.make_move(position, symbol)

            for human_move in board.get_available_moves():

                simulated_board = board.copy()
                simulated_board.make_move(human_move, "X")

                if simulated_board.check_winner() == "X":
                    return True

                if simulated_board.is_draw():
                    continue

                ai_move = ai.get_move(simulated_board)
                simulated_board.make_move(ai_move, "O")

                winner = simulated_board.check_winner()

                if winner == "X":
                    return True

                if winner == "O":
                    continue

                if simulated_board.is_draw():
                    continue

                if human_can_win(simulated_board.cells):
                    return True

            return False

        initial_board = Board()

        self.assertFalse(
            human_can_win(initial_board.cells),
            "The human found a way to defeat the AI!"
        )


if __name__ == "__main__":
    unittest.main()
