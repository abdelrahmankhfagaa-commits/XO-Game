
class Board:

    WINNING_COMBINATIONS = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    )

    def __init__(self):
        self.reset()

    @property
    def cells(self):
        return tuple(self._cells)

    def make_move(self, position: int, symbol: str) -> None:

        if type(position) is not int or not 0 <= position <= 8:
            raise ValueError("Position must be an integer between 0 and 8.")

        if symbol not in ("X", "O"):
            raise ValueError("Symbol must be X or O.")

        if not self.is_valid_move(position):
            raise ValueError("This cell is already occupied.")

        self._cells[position] = symbol

    def is_valid_move(self, position: int) -> bool:
        return (
            type(position) is int
            and 0 <= position <= 8
            and self._cells[position] == ""
        )

    def check_winner(self) -> str | None:

        for a, b, c in self.WINNING_COMBINATIONS:
            if (
                self._cells[a] != ""
                and self._cells[a] == self._cells[b] == self._cells[c]
            ):
                return self._cells[a]

        return None

    def is_draw(self) -> bool:
        return self.check_winner() is None and all(
            cell != "" for cell in self._cells
        )

    def get_available_moves(self) -> list[int]:
        return [
            index
            for index, cell in enumerate(self._cells)
            if cell == ""
        ]

    def reset(self) -> None:
        self._cells = [""] * 9

    def copy(self):
        new_board = Board()
        new_board._cells = self._cells.copy()
        return new_board
