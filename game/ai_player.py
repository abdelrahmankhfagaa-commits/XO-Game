
from game.player import Player


class AIPlayer(Player):

    def get_move(self, board, position: int | None = None) -> int:
        best_score = float("-inf")
        best_move = None

        for move in board.get_available_moves():
            simulated_board = board.copy()
            simulated_board.make_move(move, self.symbol)

            score = self._minimax(
                simulated_board,
                is_maximizing=False
            )

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def _minimax(self, board, is_maximizing: bool) -> int:

        winner = board.check_winner()

        if winner == self.symbol:
            return 1

        if winner is not None:
            return -1

        if board.is_draw():
            return 0

        if is_maximizing:
            best_score = float("-inf")

            for move in board.get_available_moves():
                simulated_board = board.copy()
                simulated_board.make_move(move, self.symbol)

                score = self._minimax(
                    simulated_board,
                    is_maximizing=False
                )

                best_score = max(best_score, score)

            return best_score

        else:
            opponent_symbol = "O" if self.symbol == "X" else "X"
            best_score = float("inf")

            for move in board.get_available_moves():
                simulated_board = board.copy()
                simulated_board.make_move(move, opponent_symbol)

                score = self._minimax(
                    simulated_board,
                    is_maximizing=True
                )

                best_score = min(best_score, score)

            return best_score
