def create_board():
  return [["1","2","3"],["4" ,"5","6"],["7","8","9"]]
def display_board(board): 
  for row in board:  
    print(row)
def get_user_move():
  user_play=int(input('which postion would you like to play: 1-9 ?'))
  return user_play
  
board=create_board()
display_board(board)
get_user_move()
