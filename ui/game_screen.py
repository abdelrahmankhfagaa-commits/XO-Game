
import tkinter as tk
from tkinter import messagebox


class GameScreen(tk.Frame):

    def __init__(self, parent, app, game, mode):

        super().__init__(parent, bg="#0F172A")

        self._app = app
        self._game = game
        self._mode = mode
        self._buttons = []

        self._create_widgets()
        self.update_board()
        self.update_scoreboard()
        self.update_status()

    def _create_widgets(self):

        title = tk.Label(
            self,
            text="TIC TAC TOE",
            font=("Arial", 26, "bold"),
            bg="#0F172A",
            fg="white"
        )
        title.pack(pady=(20, 10))

        self._status_label = tk.Label(
            self,
            text="",
            font=("Arial", 14, "bold"),
            bg="#0F172A",
            fg="#38BDF8"
        )
        self._status_label.pack(pady=10)

        # Scoreboard
        self._score_label = tk.Label(
            self,
            text="",
            font=("Arial", 12, "bold"),
            bg="#0F172A",
            fg="white"
        )
        self._score_label.pack(pady=10)

        # Game Board
        board_frame = tk.Frame(self, bg="#0F172A")
        board_frame.pack(pady=20)

        for row in range(3):
            for column in range(3):

                position = row * 3 + column

                button = tk.Button(
                    board_frame,
                    text="",
                    font=("Arial", 28, "bold"),
                    width=5,
                    height=2,
                    bg="#1E293B",
                    fg="white",
                    activebackground="#334155",
                    command=lambda p=position: self.on_cell_click(p)
                )

                button.grid(
                    row=row,
                    column=column,
                    padx=5,
                    pady=5
                )

                self._buttons.append(button)

        # Control Buttons
        controls = tk.Frame(self, bg="#0F172A")
        controls.pack(pady=15)

        tk.Button(
            controls,
            text="RESTART ROUND",
            command=self.restart_round,
            font=("Arial", 10, "bold"),
            bg="#2563EB",
            fg="white"
        ).grid(row=0, column=0, padx=5, pady=5)

        tk.Button(
            controls,
            text="RESET SCORES",
            command=self.reset_scores,
            font=("Arial", 10, "bold"),
            bg="#DC2626",
            fg="white"
        ).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(
            controls,
            text="MAIN MENU",
            command=self._app.return_to_menu,
            font=("Arial", 10, "bold"),
            bg="#475569",
            fg="white"
        ).grid(row=1, column=0, columnspan=2, pady=10)

        tk.Button(
            controls,
            text="EXIT GAME",
            command=self._app.exit_app,
            font=("Arial", 10, "bold"),
            bg="#991B1B",
            fg="white"
        ).grid(row=2, column=0, columnspan=2, pady=10)

    def on_cell_click(self, position: int):

        if self._game.game_over:
            return

        try:
            self._game.play_turn(position)

            # Computer plays immediately after the human.
            if (
                self._mode == "pvc"
                and not self._game.game_over
                and self._game.current_player.symbol == "O"
            ):
                self._game.play_turn()

        except (ValueError, RuntimeError) as error:
            messagebox.showwarning("Invalid Move", str(error))

        self.update_board()
        self.update_scoreboard()
        self.update_status()

        if self._game.game_over:
            self.show_game_over()

    def update_board(self):

        cells = self._game.board.cells

        for position, symbol in enumerate(cells):
            self._buttons[position].config(
                text=symbol,
                state="disabled" if symbol else "normal",
                disabledforeground="#38BDF8" if symbol == "X" else "#FACC15"
            )

    def update_scoreboard(self):

        scoreboard = self._app.scoreboard

        self._score_label.config(
            text=(
                f"X Wins: {scoreboard.x_wins}    "
                f"O Wins: {scoreboard.o_wins}    "
                f"Draws: {scoreboard.draws}"
            )
        )

    def update_status(self):

        self._status_label.config(
            text=self._game.get_game_status()
        )

    def restart_round(self):

        self._game.start_new_round()

        self.update_board()
        self.update_scoreboard()
        self.update_status()

    def reset_scores(self):

        confirmed = messagebox.askyesno(
            "Reset Scores",
            "Are you sure you want to reset all scores?"
        )

        if confirmed:
            self._app.scoreboard.reset_scores()
            self.update_scoreboard()

    def show_game_over(self):

        if self._game.winner:
            message = f"{self._game.winner.name} wins!"
        else:
            message = "It's a draw!"

        messagebox.showinfo("Game Over", message)
