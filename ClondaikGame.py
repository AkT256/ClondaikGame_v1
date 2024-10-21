def create_board():
  """Создает пустое поле 10 на 10"""
  board = [[' ' for col in range(10)] for row in range(10)]
  return board

def print_board(board):
  """Выводит поле на экран"""
  for row in board:
    print(row)

def make_move(board, player):
  """Игрок делает ход, ставя фишку на поле"""
  while True:
    row = int(input(f"Игрок {player}, введите номер строки (от 1 до 10): ")) - 1
    col = int(input(f"Игрок {player}, введите номер столбца (от 1 до 10): ")) - 1
    if board[row][col] == ' ':
      board[row][col] = 'X'
      return
    else:
      print("Эта клетка уже занята. Выберите другую.")

def Colx(board, row, col):
  """Проверяет, сколько в cоседних клетках 'X'"""
  count = 0
  check1 = 0
  check2 = 0
  check3 = 0
  check4 = 0
  if row - 1 < 0:
    check1 = 1
  if row + 1 > 9:
    check2 = -1
  if col - 1 < 0:
    check3 = 1
  if col + 1 > 9:
    check4 = -1
  for ir in range(-1 + check1, 2 + check2):
    for ic in range(-1 + check3, 2 + check4):
      if not (ir == ic == 0):
        new_row = row + ir
        new_col = col + ic
        if 0 <= new_row < 10 and 0 <= new_col < 10 and board[new_row][new_col] == 'X':
          count +=1
  return count

def Isx(board, row, col):
  """Проверяет, есть ли в какой-нибудь соседней клетке 'X'"""
  check1 = 0
  check2 = 0
  check3 = 0
  check4 = 0
  if row - 1 < 0:
    check1 = 1
  if row + 1 > 9:
    check2 = -1
  if col - 1 < 0:
    check3 = 1
  if col + 1 > 9:
    check4 = -1
  for ir in range(-1+check1, 2+check2):
    for ic in range(-1+check3, 2+check4):
      if not (ir == ic == 0):
        new_row = row + ir
        new_col = col + ic
        if 0 <= new_row < 10 and 0 <= new_col < 10 and board[new_row][new_col] == 'X':
          return new_row, new_col
  return False

def check_win(board):
  """Проверяет, выиграл ли игрок"""
  for row in range(10):
    for col in range(10):
      if board[row][col] == 'X':
        if Colx(board, row, col) > 1:
          return True
        elif Colx(board, row, col) == 1:
          new_row, new_col = Isx(board, row, col)
          print(new_row+1, new_col+1)
          if Colx(board,new_row, new_col) > 1:      #Больше 1 т. к. он считает ещё прошлую клетку
            return True
  return False



def main():
  """Главная функция игры"""
  board = create_board()
  current_player = 1
  while True:
    print_board(board)
    make_move(board, current_player)
    if check_win(board):
      print_board(board)
      print(f"Игрок {current_player} проиграл!")
      break
    current_player = 2 if current_player == 1 else 1

main()
