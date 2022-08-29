class Board:
    def __init__(self, width, height):
        self.width = self.set_dimension(width)
        self.height = self.set_dimension(height)
        self.board = []
        self.players = ["x", "o"]

        for j in range(self.height):
            self.board.append([])
            for i in range(self.width):
                self.board[j].append(" ")

    def print(self):
        print(" " + " ".join([str(x) for x in range(1, self.width + 1)]))
        for row in self.board:
            print("|" + "".join([x + "|" for x in row]))

    def attempt_move(self, piece, column):
        for j in range(self.height - 1, -1, -1):
            if self.board[j][column - 1] == " ":
                self.board[j][column - 1] = piece
                """ self.print() """
                return True
        raise ValueError("Error: Column {} is already full".format(column))

    def move(self, piece, column):
        if not piece in self.players:
            raise ValueError("Error: {} is not a valid piece".format(piece))
        if not column in range(1, self.width + 1):
            raise ValueError("Error: {} is not a valid column".format(column))
        self.attempt_move(piece, column)

    # Helper methods
    def set_dimension(self, v):
        try:
            if v < 4:
                raise ValueError("Error: Dimensions must be greater than 4x4")
            return int(v)
        except TypeError:
            raise TypeError("Error: Dimensions must be integers")


class Game:
    def __init__(self, width, height):
        self.board = Board(width, height)

    def move(self, piece, column):
        self.board.move(piece, column)
