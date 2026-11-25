
from game.game import Game
from game.human_player import HumanPlayer
from game.scoreboard import Scoreboard


def test_validation():

    p1 = HumanPlayer("P1", "X")
    p2 = HumanPlayer("P2", "O")

    game = Game([p1, p2], Scoreboard())

    # Test 1: Occupied cell
    game.play_turn(0)

    try:
        game.play_turn(0)
    except ValueError as error:
        print("Occupied cell:", error)

    # Test 2: Playing after game over
    for move in [3, 1, 4, 2]:
        game.play_turn(move)

    try:
        game.play_turn(8)
    except RuntimeError as error:
        print("After game over:", error)

    # Test 3: Duplicate symbols
    try:
        Game(
            [p1, HumanPlayer("P3", "X")],
            Scoreboard()
        )
    except ValueError as error:
        print("Duplicate symbols:", error)


if __name__ == "__main__":
    test_validation()
