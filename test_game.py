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
