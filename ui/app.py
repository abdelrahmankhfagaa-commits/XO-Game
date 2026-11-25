
from ui.menu_screen import MenuScreen
import tkinter as tk
from game.scoreboard import Scoreboard
from game.game import Game
from game.human_player import HumanPlayer
from game.ai_player import AIPlayer
from ui.game_screen import GameScreen
from tkinter import messagebox

class XOApp:

    def __init__(self, root: tk.Tk):

        self._root = root
        self._root.title("XO Game")
        self._root.geometry("520x750")
        self._root.minsize(520, 750)
        self._root.resizable(False, False)

        self._scoreboard = Scoreboard()
        self._current_screen = None
        self.show_menu()
        self._root.protocol("WM_DELETE_WINDOW", self.exit_app)

    @property
    def root(self):
        return self._root

    @property
    def scoreboard(self):
        return self._scoreboard

    def clear_screen(self):
        if self._current_screen is not None:
            self._current_screen.destroy()
            self._current_screen = None

    def show_menu(self):

        self.clear_screen()

        self._current_screen = MenuScreen(
            self._root,
            self
        )

        self._current_screen.pack(
            fill="both",
            expand=True
        )

    def start_game(self, mode: str):

        if mode not in ("pvp", "pvc"):
            raise ValueError("Invalid game mode.")

        player1 = HumanPlayer("Player 1", "X")

        if mode == "pvp":
            player2 = HumanPlayer("Player 2", "O")
        else:
            player2 = AIPlayer("Computer", "O")

        game = Game(
            players=[player1, player2],
            scoreboard=self._scoreboard
        )

        self.clear_screen()

        self._current_screen = GameScreen(
            self._root,
            self,
            game,
            mode
        )

        self._current_screen.pack(
            fill="both",
            expand=True
        )


    def return_to_menu(self):
        self.show_menu()

    def exit_app(self):

        confirmed = messagebox.askyesno(
            "Exit Game",
            "Are you sure you want to exit the game?"
        )

        if confirmed:
            self._root.destroy()