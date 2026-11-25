
import unittest

from game.board import Board


class TestBoard(unittest.TestCase):

    def setUp(self):
        self.board = Board()

    def test_board_starts_empty(self):
        self.assertEqual(self.board.cells, ("",) * 9)

    def test_make_valid_move(self):
        self.board.make_move(0, "X")
        self.assertEqual(self.board.cells[0], "X")

    def test_invalid_position(self):
        with self.assertRaises(ValueError):
            self.board.make_move(9, "X")

    def test_invalid_symbol(self):
        with self.assertRaises(ValueError):
            self.board.make_move(0, "A")

    def test_occupied_cell(self):
        self.board.make_move(0, "X")

        with self.assertRaises(ValueError):
            self.board.make_move(0, "O")

    def test_all_winning_combinations(self):
        for combination in Board.WINNING_COMBINATIONS:
            with self.subTest(combination=combination):
                board = Board()

                for position in combination:
                    board.make_move(position, "X")

                self.assertEqual(board.check_winner(), "X")

    def test_draw(self):
        moves = [
            (0, "X"), (1, "O"), (2, "X"),
            (3, "X"), (4, "O"), (5, "O"),
            (6, "O"), (7, "X"), (8, "X")
        ]

        for position, symbol in moves:
            self.board.make_move(position, symbol)

        self.assertTrue(self.board.is_draw())
        self.assertIsNone(self.board.check_winner())

    def test_get_available_moves(self):
        self.board.make_move(0, "X")
        self.board.make_move(4, "O")

        self.assertEqual(
            self.board.get_available_moves(),
            [1, 2, 3, 5, 6, 7, 8]
        )

    def test_reset(self):
        self.board.make_move(0, "X")
        self.board.reset()

        self.assertEqual(self.board.cells, ("",) * 9)

    def test_copy_is_independent(self):
        self.board.make_move(0, "X")

        copied_board = self.board.copy()
        copied_board.make_move(1, "O")

        self.assertEqual(self.board.cells[1], "")
        self.assertEqual(copied_board.cells[1], "O")


if __name__ == "__main__":
    unittest.main()
