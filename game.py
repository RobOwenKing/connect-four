class Board:
    def __init__(self, width, height):
        self.height = self.set_dimension(height)
        self.width = self.set_dimension(width)
        self.board = [[" " for i in range(self.width)] for j in range(self.height)]
        self.players = ["x", "o"]
        self.last_placement = ["", ""]

    def print(self):
        print(" " + " ".join([str(x) for x in range(1, self.width + 1)]))
        for row in self.board:
            print("|" + "".join([x + "|" for x in row]))

    def is_won_vertically(self, x, y, char_to_match, str_to_match):
        if self.height - y < 4 or str_to_match != "".join(
            [self.board[y + i][x] for i in range(4)]
        ):
            return False
        for i in range(4):
            self.board[y + i][x] = char_to_match.upper()
        return True

    def is_won_horizontally(self, y, char_to_match, str_to_match):
        row = "".join(self.board[y])
        if not str_to_match in row:
            return False
        start = row.find(str_to_match)
        i = 0
        while start + i < self.width and self.board[y][start + i] == char_to_match:
            self.board[y][start + i] = char_to_match.upper()
            i += 1
        return True

    def is_won_n_diagonally(self, x, y, char_to_match, str_to_match):
        min_i = -min(x, y)
        max_i = min(self.width - x, self.height - y)
        row = "".join([self.board[y + i][x + i] for i in range(min_i, max_i)])
        if str_to_match not in row:
            return False
        start = min_i + row.find(str_to_match)
        i = 0
        while (
            start + i < max_i
            and self.board[y + start + i][x + start + i] == char_to_match
        ):
            self.board[y + start + i][x + start + i] = char_to_match.upper()
            i += 1
        return True

    def is_won_p_diagonally(self, x, y, char_to_match, str_to_match):
        min_i = -min(x, self.height - y - 1)
        max_i = min(self.width - x, y + 1)
        row = "".join([self.board[y - i][x + i] for i in range(min_i, max_i)])
        if str_to_match not in row:
            return False
        start = min_i + row.find(str_to_match)
        i = 0
        while (
            start + i < max_i
            and self.board[y + start - i][x + start + i] == char_to_match
        ):
            self.board[y + start - i][x + start + i] = char_to_match.upper()
            i += 1
        return True

    def is_won(self):
        x = self.last_placement[0]
        y = self.last_placement[1]
        char_to_match = self.board[y][x]
        str_to_match = char_to_match * 4
        if (
            self.is_won_vertically(x, y, char_to_match, str_to_match)
            or self.is_won_horizontally(y, char_to_match, str_to_match)
            or self.is_won_p_diagonally(x, y, char_to_match, str_to_match)
            or self.is_won_n_diagonally(x, y, char_to_match, str_to_match)
        ):
            print(f"Congrats, {char_to_match}! You win!")
            return True
        return False

    def is_draw(self):
        if all([s.strip() for s in self.board[0]]):
            print("Game over! You drew.")
            return True
        return False

    def is_game_over(self):
        if self.is_won():
            return True
        elif self.is_draw():
            return True
        return False

    def attempt_move(self, piece, column):
        for j in range(self.height - 1, -1, -1):
            if self.board[j][column - 1] == " ":
                self.board[j][column - 1] = piece
                self.last_placement = [column - 1, j]
                return True
        raise ValueError(f"Error: Column {column} is already full")

    def move(self, piece, column):
        if not piece in self.players:
            raise ValueError(f"Error: {piece} is not a valid piece")
        if not int(column) in range(1, self.width + 1):
            raise ValueError(f"Error: {column} is not a valid column")
        self.attempt_move(piece, int(column))

    # Helper methods
    def set_dimension(self, v):
        try:
            if int(v) < 4:
                raise ValueError("Error: Dimensions must be greater than 4x4")
            return int(v)
        except TypeError:
            raise TypeError("Error: Dimensions must be integers")


class Game:
    def __init__(self):
        self.board = Board(7, 6)
        self.game_over = False
        self.players = ["x", "o"]
        self.current_player = 0
        self.play_again = True

    def move(self, piece, column):
        self.board.move(piece, column)

    def handle_move(self, col):
        try:
            self.board.move(self.players[self.current_player], col)
            self.current_player = 1 - self.current_player
            self.game_over = self.board.is_game_over()
        except Exception as e:
            print(e)

    def ask_play_again(self):
        unparsed_input = input("Would you like to play again (Y/n): ")
        self.play_again = unparsed_input.lower() not in ["n", "no", "false"]

    def start(self):
        print("WELCOME TO CONNECT FOUR!")
        while self.play_again:
            self.game_loop()
            self.ask_play_again()

    def game_loop(self):
        width = input("How many columns do you want (default 7): ") or 7
        height = input("How many rows do you want (default 6): ") or 6
        self.board = Board(width, height)
        self.game_over = False
        while not self.game_over:
            self.board.print()
            col = input(f"Pick a column, player {self.players[self.current_player]}: ")
            self.handle_move(col)
        self.board.print()


def main():
    game = Game()
    game.start()


if __name__ == "__main__":
    main()
