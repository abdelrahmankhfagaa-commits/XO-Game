from game.player import Player


class HumanPlayer(Player):

    def get_move(self, board, position: int | None = None) -> int:

        if position is None:
            raise ValueError("Human player must select a position.")

        if not board.is_valid_move(position):
            raise ValueError("Invalid move.")

        return position