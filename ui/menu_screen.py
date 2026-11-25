
import tkinter as tk


class MenuScreen(tk.Frame):

    def __init__(self, parent, app):

        super().__init__(parent, bg="#0F172A")

        self._app = app

        self._create_widgets()

    def _create_widgets(self):

        title = tk.Label(
            self,
            text="TIC TAC TOE",
            font=("Arial", 32, "bold"),
            bg="#0F172A",
            fg="white"
        )
        title.pack(pady=(100, 15))

        subtitle = tk.Label(
            self,
            text="Choose your game mode",
            font=("Arial", 13),
            bg="#0F172A",
            fg="#94A3B8"
        )
        subtitle.pack(pady=10)

        pvp_button = tk.Button(
            self,
            text="PLAYER VS PLAYER",
            font=("Arial", 14, "bold"),
            width=22,
            height=2,
            bg="#2563EB",
            fg="white",
            command=lambda: self.select_mode("pvp")
        )
        pvp_button.pack(pady=15)

        pvc_button = tk.Button(
            self,
            text="PLAYER VS COMPUTER",
            font=("Arial", 14, "bold"),
            width=22,
            height=2,
            bg="#16A34A",
            fg="white",
            command=lambda: self.select_mode("pvc")
        )
        pvc_button.pack(pady=10)

    def select_mode(self, mode: str):
        self._app.start_game(mode)
