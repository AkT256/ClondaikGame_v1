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
    row = input(f"Игрок {player}, введите номер строки (от 1 до 10): ")
    col = input(f"Игрок {player}, введите номер столбца (от 1 до 10): ")
    if (row or col) not in "12345678910":   #Если координаты не коректные, то просит выбрать другие
      print("Вводимые координаты должны быть ЧИСЛАМИ от 1 до 10! Повторите ввод: ")
      continue
    row = int(row) - 1
    col = int(col) - 1
    if row > 9 or row < 0 or col > 9 or col < 0:   #Если клетка за пределами поля, то просит выбрать другую
      print("Эта клетка за пределами поля. Выберите клетку с поля 10x10.")
      continue
    if board[row][col] == ' ':
      board[row][col] = 'X'  #Если клетка пустая то на её месте ставится 'X', иначе просит выбрать другую
      return
    else:
      print("Эта клетка уже занята. Выберите другую.")


def Colx(board, row, col):
  """Проверяет сколько в cоседних клетках 'X'"""
  count = 0   #Чеки я добавил чтобы не проверка соедних клеток не улетала за пределы поля
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
      if not (ir == ic == 0):  #Это проверка нужна чтобы одна фишка не считалась 2 раза
        new_row = row + ir  #Здесь координаты новой клетки устанавливаются, чтобы дальше проверить пустая она или нет
        new_col = col + ic
        if board[new_row][new_col] == 'X':  #проверка клетки
          count +=1
  return count

def Isx(board, row, col):
  """Проверяет есть ли в какой-нибудь соседней клетке 'X'"""
  check1 = 0   #Чеки я добавил чтобы не проверка соедних клеток не улетала за пределы поля
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
      if not (ir == ic == 0):  #Это проверка нужна чтобы одна фишка не считалась 2 раза
        new_row = row + ir  #Здесь координаты новой клетки устанавливаются, чтобы дальше проверить пустая она или нет
        new_col = col + ic
        if board[new_row][new_col] == 'X':  #проверка клетки
          return new_row, new_col  #Возвращает координаты соседней клетки в которой есть 'X'(Эта функция специально прекращается после 1 найденной фишки т. к. она используется только в случае если у фишки только 1 сосед)
  return False

def check_win(board):
  """Проверяет, выиграл ли игрок"""
  for row in range(10):
    for col in range(10):
      if board[row][col] == 'X':
        if Colx(board, row, col) > 1:  #Если больше 1 соседа то проигрыш
          return True
        elif Colx(board, row, col) == 1: #Если 1 сосед то дальше идёт проверка сколько соседей у этого соседа
          new_row, new_col = Isx(board, row, col)
          if Colx(board,new_row, new_col) > 1:      #Больше 1(а не 0) т. к. он считает ещё прошлую клетку
            return True
  return False



def main():
  """Главная функция игры"""
  board = create_board()
  current_player = 1   #Изначально ходит 1 игрок
  while True:  #Игра продолжается до проигрыша 1 из игроков
    print_board(board)
    make_move(board, current_player)
    if check_win(board):
      print_board(board)
      print(f"Игрок {current_player} проиграл!")
      break
    current_player = 2 if current_player == 1 else 1    #Это чтобы было понятно какой игрок ходит

main()
