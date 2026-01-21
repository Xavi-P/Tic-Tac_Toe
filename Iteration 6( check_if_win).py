def display_board(board): 
  for row in board:
    print(row)
  return board
def get_user_move(guesses):
  
  user_play=(input('which postion would you like to play: 1-9 ?'))
  while user_play not in ["1","2","3","4","5","6","7","8","9"]:
    user_play=(input("incorrect input: please enter a value 1-9"))
  while user_play in guesses or user_play not in ["1","2","3","4","5","6","7","8","9"]:
    user_play=(input("incorrect input: please enter a unoccupied posistion"))
  
  guesses.append(user_play)
  return user_play,guesses
  
def place_move(board,user_play):
  user_play=int(user_play)
  if user_play<=3 and user_play>0:
    board[0].pop(user_play-1)
    board[0].insert(user_play-1,"X")
  elif user_play<=6 and user_play>3:
    board[1].pop(user_play-4)
    board[1].insert(user_play-4,"X")
  elif user_play<=9 and user_play>6:
    board[2].pop(user_play-7)
    board[2].insert(user_play-7,"X")
  return board
def check_winner(board,player_symbol):
  Win=False
  if board[0][0] == player_symbol and board[1][0] == player_symbol and board[2][0] == player_symbol:
    Win=True
     
  elif board[0][1] == player_symbol and board[1][1] == player_symbol and board[2][1] == player_symbol:
    Win=True
   
  elif board[0][2] == player_symbol and board[1][2] == player_symbol and board[2][2] == player_symbol:
    Win=True
    
  elif board[0][0] == player_symbol and board[0][1] == player_symbol and board[0][2] == player_symbol:
    Win=True
    
  elif board[1][0] == player_symbol and board[1][1] == player_symbol and board[1][2] == player_symbol:
    Win=True
    
  elif board[2][0] == player_symbol and board[2][1] == player_symbol and board[2][2] == player_symbol:
    Win=True
    
  elif board[0][2] == player_symbol and board[1][1] == player_symbol and board[2][0] == player_symbol:
    Win=True
    
  elif board[0][0] == player_symbol and board[1][1] == player_symbol and board[2][2] == player_symbol:
    Win=True
    
  if Win is True:
    print("congrats u won")
  return Win
player_symbol='X'
play=True
Moves=[]
board=[["1","2","3"],["4" ,"5","6"],["7","8","9"]]
while play:
  display_board(board)
  user_play, Moves=get_user_move(Moves)
  print("Moves:" +str(Moves))
  place_move(board,user_play)
  Win=check_winner(board,player_symbol)
  if Win== True:
    play=False
