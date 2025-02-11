
class Game:
    def __init__(self):
        # Initialize game state
        self.board = [' '] * 9
        self.current_player = 'X'

    def display_board(self):
        # Display the current state of the board
        for i in range(0, 9, 3):
            print(self.board[i] + '|' + self.board[i+1] + '|' + self.board[i+2])
            if i < 6:
                print('-----')

    def make_move(self, position):
        # Make a move on the board
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("Position already taken!")

    def check_winner(self):
        # Check for a winner
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]
        return None

    def is_draw(self):
        # Check for a draw
        return ' ' not in self.board

# Example usage
if __name__ == "__main__":
    game = Game()
    game.display_board()
    game.make_move(0)
    game.display_board()
