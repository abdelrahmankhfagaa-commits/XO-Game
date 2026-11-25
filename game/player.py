
from abc import ABC, abstractmethod


class Player(ABC):

    def __init__(self, name: str, symbol: str):
        if not name or not name.strip():
            raise ValueError("Player name cannot be empty.")

        if symbol not in ("X", "O"):
            raise ValueError("Player symbol must be X or O.")

        self._name = name.strip()
        self._symbol = symbol

    @property
    def name(self) -> str:
        return self._name

    @property
    def symbol(self) -> str:
        return self._symbol

    @abstractmethod
    def get_move(self, board, position: int | None = None) -> int:
        pass
