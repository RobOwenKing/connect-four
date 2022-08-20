from io import StringIO
from contextlib import redirect_stdout
from unittest import TestCase
from unittest.mock import patch
import game


class TestBoard(TestCase):
    def test_init_narrow_board(self):
        with StringIO() as output, redirect_stdout(output):
            board = game.Board(2, 3)
            board.print()
            self.assertEqual(output.getvalue(), " 1 2\n| | |\n| | |\n| | |\n")

    def test_init_wide_board(self):
        with StringIO() as output, redirect_stdout(output):
            board = game.Board(3, 2)
            board.print()
            self.assertEqual(output.getvalue(), " 1 2 3\n| | | |\n| | | |\n")

    def test_single_move(self):
        with StringIO() as output, redirect_stdout(output):
            board = game.Board(3, 3)
            board.move("x", 1)
            board.print()
            self.assertEqual(output.getvalue(), " 1 2 3\n| | | |\n| | | |\n|x| | |\n")

    def test_multiple_moves(self):
        with StringIO() as output, redirect_stdout(output):
            board = game.Board(3, 3)
            board.move("x", 1)
            board.move("o", 1)
            board.move("x", 1)
            board.move("o", 2)
            board.print()
            self.assertEqual(output.getvalue(), " 1 2 3\n|x| | |\n|o| | |\n|x|o| |\n")

    def test_full_column_error(self):
        board = game.Board(3, 2)
        board.move("x", 1)
        board.move("o", 1)
        with self.assertRaises(ValueError):
            board.move("x", 1)

    def test_invalid_piece(self):
        board = game.Board(2, 2)
        with self.assertRaises(ValueError):
            board.move("a", 1)
