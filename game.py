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

    def is_won(self):
        print("Win!")

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
                """ self.print() """
                return True
        raise ValueError("Error: Column {} is already full".format(column))

    def move(self, piece, column):
        if not piece in self.players:
            raise ValueError("Error: {} is not a valid piece".format(piece))
        if not int(column) in range(1, self.width + 1):
            raise ValueError("Error: {} is not a valid column".format(column))
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
    def __init__(self, width=7, height=6):
        self.board = Board(width, height)
        self.game_over = False
        self.players = ["x", "o"]
        self.current_player = 0

    def move(self, piece, column):
        self.board.move(piece, column)

    def handle_move(self, col):
        try:
            self.board.move(self.players[self.current_player], col)
            self.board.print()
            self.current_player = 1 - self.current_player
            self.game_over = self.board.is_game_over()
        except Exception as e:
            print(e)

    def loop(self):
        self.board.print()
        while not self.game_over:
            col = input(
                "Pick a column, player {}: ".format(self.players[self.current_player])
            )
            self.handle_move(col)


print("WELCOME TO CONNECT FOUR!")
width = input("How many columns do you want (default 7): ")
height = input("How many rows do you want (default 6): ")

game = Game(width, height)
game.loop()
