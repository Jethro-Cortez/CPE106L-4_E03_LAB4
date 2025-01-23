import random
import oxo_data


class Game:
    def __init__(self):
        self.board = self.new_game()

    def new_game(self):
        """Create a new empty game."""
        return list(" " * 9)

    def save_game(self):
        """Save the current game state to disk."""
        oxo_data.saveGame(self.board)

    def restore_game(self):
        """Restore the previously saved game."""
        try:
            restored = oxo_data.restoreGame()
            if len(restored) == 9:
                self.board = restored
            else:
                self.board = self.new_game()
        except IOError:
            self.board = self.new_game()

    def generate_move(self):
        """Generate a random valid move."""
        options = [i for i in range(len(self.board)) if self.board[i] == " "]
        return random.choice(options) if options else -1

    def is_winning_move(self):
        """Check if the current board state contains a winning line."""
        wins = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        )
        for a, b, c in wins:
            chars = self.board[a] + self.board[b] + self.board[c]
            if chars == "XXX" or chars == "OOO":
                return True
        return False

    def user_move(self, cell):
        """Process the user's move."""
        if self.board[cell] != " ":
            raise ValueError("Invalid cell")
        self.board[cell] = "X"
        return "X" if self.is_winning_move() else ""

    def computer_move(self):
        """Process the computer's move."""
        cell = self.generate_move()
        if cell == -1:
            return "D"  # Draw
        self.board[cell] = "O"
        return "O" if self.is_winning_move() else ""