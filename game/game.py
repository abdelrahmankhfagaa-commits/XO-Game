
from game.board import Board
from game.scoreboard import Scoreboard
from game.player import Player


class Game:

    def __init__(self, players: list[Player], scoreboard: Scoreboard):

        if len(players) != 2:
            raise ValueError("A game must have exactly two players.")

        if players[0].symbol == players[1].symbol:
            raise ValueError("Players must have different symbols.")

        if {player.symbol for player in players} != {"X", "O"}:
            raise ValueError("Players must use X and O.")

        self._board = Board()
        self._players = players
        self._current_player = players[0]
        self._scoreboard = scoreboard
        self._game_over = False
        self._winner = None

    @property
    def board(self) -> Board:
        return self._board

    @property
    def current_player(self) -> Player:
        return self._current_player

    @property
    def game_over(self) -> bool:
        return self._game_over

    @property
    def winner(self) -> Player | None:
        return self._winner

    def play_turn(self, position: int | None = None) -> None:

        if self._game_over:
            raise RuntimeError("The game is already over.")

        move = self._current_player.get_move(
            self._board,
            position
        )

        self._board.make_move(
            move,
            self._current_player.symbol
        )

        winner_symbol = self._board.check_winner()

        if winner_symbol is not None:
            self._winner = self._current_player
            self._game_over = True
            self._scoreboard.record_win(winner_symbol)
            return

        if self._board.is_draw():
            self._game_over = True
            self._scoreboard.record_draw()
            return

        self.switch_player()

    def switch_player(self) -> None:
        self._current_player = (
            self._players[1]
            if self._current_player is self._players[0]
            else self._players[0]
        )

    def start_new_round(self) -> None:
        self._board.reset()
        self._current_player = self._players[0]
        self._game_over = False
        self._winner = None

    def get_game_status(self) -> str:

        if self._winner is not None:
            return f"{self._winner.name} wins!"

        if self._game_over:
            return "It's a draw!"

        return f"{self._current_player.name}'s turn"
