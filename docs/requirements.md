# XO Game — Software Requirements Specification

## 1. Project Overview

XO Game is a desktop Tic-Tac-Toe application developed using Python and Tkinter.

The application supports two game modes:
- Player vs Player (PvP)
- Player vs Computer (PvC)

The computer opponent uses the Minimax algorithm to make optimal decisions and cannot be defeated when implemented correctly.

## 2. Project Objectives

- Apply Object-Oriented Programming principles.
- Build a desktop GUI using Tkinter.
- Implement an unbeatable AI opponent using Minimax.
- Apply software design principles, including SOLID.
- Practice unit testing and software validation.
- Build a maintainable and extensible application.

## 3. Functional Requirements

| ID | Requirement |
|---|---|
| FR-01 | The application shall display a main menu. |
| FR-02 | The user shall be able to select Player vs Player or Player vs Computer. |
| FR-03 | The game board shall contain 9 cells arranged in a 3×3 grid. |
| FR-04 | X shall always make the first move. |
| FR-05 | In PvP mode, Player 1 shall use X and Player 2 shall use O. |
| FR-06 | In PvC mode, the human player shall use X and the computer shall use O. |
| FR-07 | The application shall prevent selecting an occupied cell. |
| FR-08 | The application shall detect winning combinations and draw situations. |
| FR-09 | The application shall prevent additional moves after a round ends. |
| FR-10 | The computer shall choose its moves using the Minimax algorithm. |
| FR-11 | The scoreboard shall track X Wins, O Wins, and Draws during the current application session. |
| FR-12 | The user shall be able to restart a round, reset scores, and return to the main menu. |

## 4. Game Rules

- The board consists of 3 rows and 3 columns.
- Players alternate turns.
- X always starts.
- A player wins by completing three matching symbols horizontally, vertically, or diagonally.
- A round ends when a player wins or all cells become occupied.
- A draw occurs when all cells are occupied without a winner.

## 5. Scoreboard Requirements

The scoreboard shall track:

- X Wins
- O Wins
- Draws

Additional rules:

- Restarting a round shall not reset the scoreboard.
- Resetting scores shall require user confirmation.
- Returning to the main menu shall not reset the scoreboard.
- Scores shall remain available during the current application session only.
- Scores shall not be saved after the application closes.

## 6. AI Requirements

- The computer shall use the Minimax algorithm.
- The computer shall select an optimal available move.
- The computer shall never select an occupied cell.
- The computer shall only play after a valid human move.
- The computer shall not make moves after the round ends.

## 7. User Interface Requirements

The application shall provide:

- A modern and clear desktop interface.
- A main menu for selecting the game mode.
- A 3×3 interactive game board.
- A scoreboard displaying the current results.
- A status message indicating the current turn or round result.
- Controls for restarting the round, resetting scores, and returning to the menu.

## 8. Validation and Error Handling

The application shall:

- Reject invalid cell selections.
- Prevent overwriting existing moves.
- Prevent moves after a round has ended.
- Validate game state before accepting a move.
- Handle reset and restart actions safely.
- Maintain consistency between the game logic and the displayed interface.

## 9. Non-Functional Requirements

### Usability
The interface should be simple, clear, and easy to use.

### Reliability
The application should handle valid and invalid actions correctly.

### Maintainability
The code should be organized into separate modules with clear responsibilities.

### Extensibility
The design should allow future features without major changes to existing components.

### Readability
The code should follow consistent naming conventions and use meaningful documentation.

### Testability
Core game logic and AI behavior should be testable independently of the graphical interface.

## 10. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Tkinter | Desktop graphical interface |
| OOP | Application architecture |
| Minimax | AI decision-making algorithm |
| unittest | Unit testing |
| Git | Version control |
| GitHub | Source code hosting and collaboration |

## 11. Out of Scope

The following features are not included in version 1:

- Online multiplayer.
- User accounts and authentication.
- Database integration.
- Persistent score storage.
- Online leaderboards.

## 12. Acceptance Criteria

| ID | Acceptance Criterion |
|---|---|
| AC-01 | The application launches and displays the main menu. |
| AC-02 | The user can start either supported game mode. |
| AC-03 | The board displays exactly nine playable cells. |
| AC-04 | X always starts each new round. |
| AC-05 | Occupied cells cannot be selected again. |
| AC-06 | The application correctly detects wins and draws. |
| AC-07 | No moves are accepted after a round ends. |
| AC-08 | The AI makes optimal moves using Minimax. |
| AC-09 | Restarting a round preserves the scoreboard. |
| AC-10 | Resetting scores clears all scoreboard values after confirmation. |

## 13. Project Scope Summary

XO Game is a single-session desktop application focused on demonstrating Object-Oriented Programming, software design, algorithm implementation, graphical user interfaces, and software testing through a complete playable Tic-Tac-Toe game.