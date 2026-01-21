def play_game(): 
  play=True
  alternation=1
  Moves=[]
  board=[["1","2","3"],["4" ,"5","6"],["7","8","9"]]
  
  return play, Moves, board, alternation

def Get_user_symbol():
  player_symbol=input("What would you like for your symbol: O or X ?")
  while player_symbol not in ["x","o","X","O"]:
    player_symbol=input(" invalid choise: please enter either X or O")
  while player_symbol=="x":
    player_symbol="X"
  while player_symbol=="o":
   player_symbol="O"
  
  
  if player_symbol=="O":
    player2_symbol="X"
  elif player_symbol=="X":
    player2_symbol="O"
  return player_symbol, player2_symbol



def display_board(board): 
  for row in board:
    print(row)
  return board

def get_user_move(guesses):
  if alternation%2==0:
    print("Player %s's turn:" %(player2_symbol))
  else:
    print("Player %s's turn:" % (player_symbol))
  user_play=(input('which postion would you like to play: 1-9 ?'))
  
  while user_play not in ["1","2","3","4","5","6","7","8","9"]:
    user_play=(input("incorrect input: please enter a value 1-9"))
  while user_play in guesses or user_play not in ["1","2","3","4","5","6","7","8","9"]:
    user_play=(input("incorrect input: please enter a unoccupied posistion"))
  os.system("cls")
  guesses.append(user_play)
  return user_play,guesses
  
def place_move(board,user_play,player_symbol,player2_symbol,alternation):
  user_play=int(user_play)
  alternation=alternation+1

  if alternation%2==0:
    if user_play<=3 and user_play>0:
      board[0].pop(user_play-1)
      board[0].insert(user_play-1,player_symbol)
    elif user_play<=6 and user_play>3:
      board[1].pop(user_play-4)
      board[1].insert(user_play-4,player_symbol)
    elif user_play<=9 and user_play>6:
      board[2].pop(user_play-7)
      board[2].insert(user_play-7,player_symbol)
  else:
    if user_play<=3 and user_play>0:
      board[0].pop(user_play-1)
      board[0].insert(user_play-1,player2_symbol)
    elif user_play<=6 and user_play>3:
      board[1].pop(user_play-4)
      board[1].insert(user_play-4,player2_symbol)
    elif user_play<=9 and user_play>6:
      board[2].pop(user_play-7)
      board[2].insert(user_play-7,player2_symbol)
  return board, alternation


def check_winner(board,player_symbol,player2_symbol):
  Win=False
  Win2=False
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
  
  
  if board[0][0] == player2_symbol and board[1][0] == player2_symbol and board[2][0] == player2_symbol:
    Win2=True
     
  elif board[0][1] == player2_symbol and board[1][1] == player2_symbol and board[2][1] == player2_symbol:
    Win2=True
   
  elif board[0][2] == player2_symbol and board[1][2] == player2_symbol and board[2][2] == player2_symbol:
    Win2=True
    
  elif board[0][0] == player2_symbol and board[0][1] == player2_symbol and board[0][2] == player2_symbol:
    Win2=True
    
  elif board[1][0] == player2_symbol and board[1][1] == player2_symbol and board[1][2] == player2_symbol:
    Win2=True
    
  elif board[2][0] == player2_symbol and board[2][1] == player2_symbol and board[2][2] == player2_symbol:
    Win2=True
    
  elif board[0][2] == player2_symbol and board[1][1] == player2_symbol and board[2][0] == player2_symbol:
    Win2=True
    
  elif board[0][0] == player2_symbol and board[1][1] == player2_symbol and board[2][2] == player2_symbol:
    Win2=True
  
  if Win is True:
    print("congrats %s:you won" % (player_symbol))
  elif Win2 is True:
    print("congrats %s :you won"% (player2_symbol))
  return Win, Win2
  
def check_tie(board,Win, Win2):
  if Win==True or Win2==True:
    return False
  elif board[0][0] in ["X","O"] and board[0][1] in ["X","O"] and board[0][2] in ["X","O"] and board[1][0] in ["X","O"] and board[1][1] in ["X","O"] and board[1][2] in ["X","O"] and board[2][0]  in ["X","O"] and board[2][1] in ["X","O"] and board[2][2]in ["X","O"] and board[0][0] in ["X","O"]:
    print("Round over: Tie")
    return True
  

import os
play, Moves, board,alternation =play_game()
player_symbol, player2_symbol=Get_user_symbol()

while play:
  display_board(board)
  
  user_play, Moves=get_user_move(Moves)
  
  print("Moves:" +str(Moves))
  
  board, alternation=place_move(board,user_play,player_symbol,player2_symbol,alternation)
  
  Win, Win2=check_winner(board,player_symbol,player2_symbol)
  Tie=check_tie(board,Win, Win2)
  if Win== True or Win2== True or Tie==True:
    play=False
    display_board(board)
