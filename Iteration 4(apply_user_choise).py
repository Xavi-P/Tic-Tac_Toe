def create_board():
  return [["1","2","3"],["4" ,"5","6"],["7","8","9"]]
  
def display_board(board): 
  for row in board:
    print(row)

def get_user_move():
  user_play=int(input('which postion would you like to play: 1-9 ?'))
  return user_play

def place_move(board,user_play):
  if user_play<=3 and user_play>0:
    board[0].pop(user_play-1)
    board[0].insert(user_play-1,"X")
  elif user_play<=6 and user_play>3:
    board[1].pop(user_play-4)
    board[1].insert(user_play-4,"X")
  elif user_play<=9 and user_play>6:
    board[2].pop(user_play-7)
    board[2].insert(user_play-7,"X")
  else:
    print("invalid input, please enter a value 1-9")
board=create_board()
display_board(board)
user_play=get_user_move()
place_move(board,user_play)
display_board(board)
