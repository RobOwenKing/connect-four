class Connect4Board:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.board = []
    self.players = ['x', 'o']

    for j in range(height):
      self.board.append([])
      for i in range(width):
        self.board[j].append(' ')

  def print(self):
    print(' ' + ' '.join([str(x) for x in range(1, self.width + 1)]))
    for row in self.board:
      print('|' + ''.join([x + '|' for x in row]))

  def attempt_move(self, piece, column):
    for j in range(self.height-1, -1, -1):
      if self.board[j][column-1] == ' ':
        self.board[j][column-1] = piece
        self.print()
        return
    print('Error: Column {} is already full'.format(column))

  def move(self, piece, column):
    if not piece in self.players: return print('Error: {} is not a valid piece'.format(piece))
    if not column in range(1, self.width+1): return print('Error: {} is not a valid column'.format(column))
    self.attempt_move(piece, column)

# TESTS
test = Connect4Board(3, 3)

# Ordinary piece placement works
test.move('x', 1)
test.move('o', 1)
test.move('x', 1)
test.move('o', 2)

# Trying to play in a full column gives an error
test.move('x', 1)

# Trying to play an invalid piece gives an error
test.move('a', 2)

# Trying to play an invalid column gives an error
test.move('x', 0)
test.move('x', 4)
test.move('x', 2.5)

print(all(' '))
