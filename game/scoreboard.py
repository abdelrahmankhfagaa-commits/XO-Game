
class Scoreboard:

    def __init__(self):
        self.reset_scores()

    def record_win(self, symbol: str) -> None:

        if symbol == "X":
            self._x_wins += 1

        elif symbol == "O":
            self._o_wins += 1

        else:
            raise ValueError("Winner symbol must be X or O.")

    def record_draw(self) -> None:
        self._draws += 1

    def reset_scores(self) -> None:
        self._x_wins = 0
        self._o_wins = 0
        self._draws = 0

    @property
    def x_wins(self) -> int:
        return self._x_wins

    @property
    def o_wins(self) -> int:
        return self._o_wins

    @property
    def draws(self) -> int:
        return self._draws
