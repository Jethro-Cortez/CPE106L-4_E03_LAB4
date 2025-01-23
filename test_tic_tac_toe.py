import unittest
from oxo_logic import Game


class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        """Set up a fresh game before each test."""
        self.game = Game()

    def test_new_game(self):
        """Test that a new game initializes with an empty board."""
        self.assertEqual(self.game.new_game(), [" "] * 9)

    def test_user_move_valid(self):
        """Test a valid user move."""
        self.game.user_move(0)
        self.assertEqual(self.game.board[0], "X")

    def test_user_move_invalid(self):
        """Test an invalid user move (cell already occupied)."""
        self.game.board[0] = "X"
        with self.assertRaises(ValueError):
            self.game.user_move(0)

    def test_computer_move(self):
        """Test that the computer places a mark in an empty cell."""
        self.game.computer_move()
        self.assertIn("O", self.game.board)

    def test_computer_move_draw(self):
        """Test that the computer declares a draw when no moves are available."""
        self.game.board = ["X", "O", "X", "X", "O", "X", "O", "X", "O"]
        result = self.game.computer_move()
        self.assertEqual(result, "D")

    def test_is_winning_move(self):
        """Test identifying a winning board state."""
        self.game.board = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
        self.assertTrue(self.game.is_winning_move())

    def test_is_not_winning_move(self):
        """Test identifying a non-winning board state."""
        self.game.board = ["X", "O", "X", " ", " ", " ", " ", " ", " "]
        self.assertFalse(self.game.is_winning_move())


if __name__ == "__main__":
    unittest.main()