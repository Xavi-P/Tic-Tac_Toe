import os
import random
def play_game():
  play=True
  alternation=1
  Moves=[]
  board=[["1","2","3"],["4" ,"5","6"],["7","8","9"]]
  return play, Moves, board, alternation


def display_board(board):
  for row in board:
    highlight = []
    for position in row:
      if position == "X" or position == "O":
        highlight.append("[" + position + "]")
      else:
        highlight.append(" " + position + " ")

    print(highlight)
  return board


def CPU_or_person():
  choise=input("How many players?: 1 or 2?")
  while choise not in ["1","2"]:
    choise=input("invalid input: 1 or 2 players?")
  if choise=="1":
    return True
  else:
    return False


def CPU_move(Moves):
  CPU_play=str(random.randint(1,9))
  while CPU_play in Moves:
    CPU_play=str(random.randint(1,9))
  Moves.append(CPU_play)
  print("Moves:"+str(Moves))
  print("")
  return CPU_play, Moves


def get_user_move(Moves, alternation, player):
  if alternation%2==0:
    print("Player O's turn:")
  else:
    print("Player X's turn:")

  user_play=(input('which postion would you like to play: 1-9 ?'))

  while user_play not in ["1","2","3","4","5","6","7","8","9"]:
    user_play=(input("incorrect input: please enter a value 1-9"))

  while user_play in Moves:
    user_play=(input("incorrect input: please enter a unoccupied posistion"))

  while user_play in Moves or user_play not in ["1","2","3","4","5","6","7","8","9"]:
    user_play=(input("incorrect input: please enter a unoccupied posistion and number 1-9"))

  os.system("cls")
  Moves.append(user_play)
  print("Moves:"+str(Moves))
  print("")
  return user_play, Moves


def place_move(board,user_play,alternation):
  user_play=int(user_play)
  alternation=alternation+1

  if alternation%2==0:
    symbol="X"
  else:
    symbol="O"

  if user_play<=3 and user_play>0:
    board[0][user_play-1]=symbol
  elif user_play<=6 and user_play>3:
    board[1][user_play-4]=symbol
  elif user_play<=9 and user_play>6:
    board[2][user_play-7]=symbol

  return board, alternation


def check_winner(board,player):
  Win=False
  Win2=False

  if board[0][0]=="X" and board[1][0]=="X" and board[2][0]=="X":
    Win=True
  elif board[0][1]=="X" and board[1][1]=="X" and board[2][1]=="X":
    Win=True
  elif board[0][2]=="X" and board[1][2]=="X" and board[2][2]=="X":
    Win=True
  elif board[0][0]=="X" and board[0][1]=="X" and board[0][2]=="X":
    Win=True
  elif board[1][0]=="X" and board[1][1]=="X" and board[1][2]=="X":
    Win=True
  elif board[2][0]=="X" and board[2][1]=="X" and board[2][2]=="X":
    Win=True
  elif board[0][2]=="X" and board[1][1]=="X" and board[2][0]=="X":
    Win=True
  elif board[0][0]=="X" and board[1][1]=="X" and board[2][2]=="X":
    Win=True

  if board[0][0]=="O" and board[1][0]=="O" and board[2][0]=="O":
    Win2=True
  elif board[0][1]=="O" and board[1][1]=="O" and board[2][1]=="O":
    Win2=True
  elif board[0][2]=="O" and board[1][2]=="O" and board[2][2]=="O":
    Win2=True
  elif board[0][0]=="O" and board[0][1]=="O" and board[0][2]=="O":
    Win2=True
  elif board[1][0]=="O" and board[1][1]=="O" and board[1][2]=="O":
    Win2=True
  elif board[2][0]=="O" and board[2][1]=="O" and board[2][2]=="O":
    Win2=True
  elif board[0][2]=="O" and board[1][1]=="O" and board[2][0]=="O":
    Win2=True
  elif board[0][0]=="O" and board[1][1]=="O" and board[2][2]=="O":
    Win2=True

  if Win and player==True:
    print("CPU won:you lost")
  elif Win:
    print("congrats X :you won")
  elif Win2:
    print("congrats O :you won")

  return Win, Win2


def check_tie(board,Win,Win2):
  if Win or Win2:
    return False

  for row in board:
    for position in row:
      if position not in ["X","O"]:
        return False
  
  print("Round over: Tie")
  return True


X_wins = 0
O_wins = 0
ties = 0

play, Moves, board, alternation = play_game()
player = CPU_or_person()

while play:

  while player==True:
    CPU_play, Moves = CPU_move(Moves)
    board, alternation = place_move(board, CPU_play, alternation)
    Win, Win2 = check_winner(board,player)
    Tie = check_tie(board, Win, Win2)
    display_board(board)

    if Win or Win2 or Tie:
      if Win:
        X_wins += 1
      elif Win2:
        O_wins += 1
      elif Tie:
        ties += 1

      print("Scoreboard:")
      print("X wins:", X_wins)
      print("O wins:", O_wins)
      print("Ties:", ties)

      play_again=input("would you like to play again? y, n")
      if play_again == "y":
        play, Moves, board, alternation = play_game()
        continue
      else:
        print("bye bye")
        play=False
        break

    user_play, Moves = get_user_move(Moves, alternation, player)
    board, alternation = place_move(board, user_play, alternation)

  else:
    display_board(board)
    user_play, Moves = get_user_move(Moves, alternation, player)
    board, alternation = place_move(board, user_play, alternation)

  Win, Win2 = check_winner(board,player)
  Tie = check_tie(board, Win, Win2)

  if Win or Win2 or Tie:
    if Win:
      X_wins += 1
    elif Win2:
      O_wins += 1
    elif Tie:
      ties += 1

    display_board(board)

    print("Scoreboard:")
    print("X wins:", X_wins)
    print("O wins:", O_wins)
    print("Ties:", ties)

    play_again=input("would you like to play again? y, n")
    if play_again == "y":
      play, Moves, board, alternation = play_game()
    else:
      print("bye bye")
      play=False
