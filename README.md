# XO Game — Tic-Tac-Toe

A Python-based Tic-Tac-Toe game built with **Object-Oriented Programming (OOP)** and **Tkinter**, featuring both Human vs. Human and Human vs. AI gameplay. The AI uses the **Minimax algorithm** to make optimal decisions.

## Features

- **Two Game Modes**
  - Player vs. Player (PvP).
  - Player vs. Computer (PvC).

- **AI Opponent**
  - Uses the Minimax algorithm.
  - Evaluates possible game states to choose optimal moves.

- **Graphical User Interface**
  - Built with Python Tkinter.
  - Main menu and game screens.
  - Interactive 3×3 game board.

- **Scoreboard**
  - Tracks X wins, O wins, and draws during the session.
  - Restart a round without losing the current scores.
  - Reset scores with confirmation.

- **Game Validation**
  - Prevents moves in occupied cells.
  - Prevents moves after a game has ended.
  - Ensures the AI only responds to valid human moves.

## OOP Concepts Applied

This project demonstrates several Object-Oriented Programming principles:

- **Encapsulation:** Protecting internal object state and providing controlled access through methods and properties.
- **Abstraction:** Defining common player behavior through an abstract base class.
- **Inheritance:** Implementing `HumanPlayer` and `AIPlayer` as subclasses of `Player`.
- **Polymorphism:** Supporting different player implementations through a shared interface.
- **Composition:** Organizing game components such as the board, players, and scoreboard into a working game system.

## Project Structure

```text
XO-Game/
│
├── docs/
│   ├── Class_diagram.drawio
│   └── requirements.md
│
├── game/
│   ├── ai_player.py
│   ├── board.py
│   ├── game.py
│   ├── human_player.py
│   ├── player.py
│   └── scoreboard.py
│
├── tests/
│   ├── test_ai.py
│   ├── test_board.py
│   ├── test_game.py
│   ├── test_players.py
│   ├── test_scoreboard.py
│   └── test_validation_manual.py
│
├── ui/
│   ├── app.py
│   ├── game_screen.py
│   └── menu_screen.py
│
├── main.py
├── .gitignore
└── README.md
```

## Requirements

- Python 3 installed.
- Tkinter (usually included with standard Python installations).

No external Python packages are required.

## Installation & Usage

### 1. Clone the repository

```bash
git clone https://github.com/abdelrahmankhfagaa-commits/XO-Game.git
```

### 2. Navigate to the project directory

```bash
cd XO-Game
```

### 3. Run the application

```bash
python main.py
```

## Running Tests

The project includes unit tests for the main game components.

Run the test suite using:

```bash
python -m unittest discover -s tests -v
```

## Documentation

- [Requirements Document](docs/requirements.md)
- [UML Class Diagram](docs/Class_diagram.drawio)

## Project Goals

This project was developed as a practical application of Object-Oriented Programming concepts, software design, validation, and testing in Python.

It aims to demonstrate how to structure a small application into separate components while keeping responsibilities organized and maintainable.

---

## Author

**Abdelrahman Khfaga**

Computer and Control Systems Engineering Student  
Faculty of Engineering — Mansoura University

- **GitHub:** [abdelrahmankhfagaa-commits](https://github.com/abdelrahmankhfagaa-commits)
- **LinkedIn:** [Abdelrahman Khfaga](https://www.linkedin.com/in/abdelrahman-khfaga-8b9191337/)

---

**Designed and developed with Python, OOP, Tkinter, and Minimax.**
