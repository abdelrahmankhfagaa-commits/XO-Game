import tkinter as tk

from ui.app import XOApp


def main():

    root = tk.Tk()

    app = XOApp(root)

    root.mainloop()


if __name__ == "__main__":
    main()