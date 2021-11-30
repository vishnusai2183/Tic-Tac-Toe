
# creating board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#check if game continues
game_continue = True 

winner = None
#first player is X
present_player = "X"

#function to display board
def display_board():
  print(board[0] + "  |  " + board[1] + "  |  " + board[2] +"    1 | 2 | 3")         
  print(board[3] + "  |  " + board[4] + "  |  " + board[5] +"    4 | 5 | 6" )         
  print(board[6] + "  |  " + board[7] + "  |  " + board[8] +"    7 | 8 | 9" )         
 
# Play a game of tic tac toe
def play_ttt():

    # Show the initial game board
    display_board()

    # Loop until we find winner
    while game_continue:

        # Handle a turn
        choose_position(present_player)

        # Check if the game is over
        check_game_over()

        # Flip to the other player
        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " has won 😊.")
    elif winner == None:
        print("the game is Tie 🙂.") 




def choose_position(player):
  position=input("Choose your position from 1 to 9 for " + player + ":")
  
  valid = False
  while not valid:
   while position not in ["1","2","3","4","5","6","7","8","9"]:
      
      position=input("Choose a correct position from 1 to 9 for " + player + ":")
  
   position = int(position) - 1 
   
   if board[position] == "-":
     valid=True
   else :
     print("you can't override. Go again")
  
  board[position]= player

  
  display_board()


def check_game_over():
  check_win()
  check_tie()

def check_win():
  
  global winner
  
  
  #check rows
  row_winner=check_row()
  #check coloum
  coloum_winner=check_coloum()
  #check diagonal
  diagonal_winner=check_diagonal()

  if row_winner:
    winner=row_winner
  elif coloum_winner:
    winner=coloum_winner
  elif diagonal_winner:
    winner=diagonal_winner
  else: 
    winner=None  
  return

def check_row():
  global game_continue
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  #if there is win we are stopping the while loop
  if row_1 or row_2 or row_3:
    game_continue = False
  #return winner(X or O)
  if row_1:
    return board[0]
  if row_2:
    return board[3]
  if row_3:
    return board[6]
  return

def check_coloum():
  global game_continue
  coloum_1 = board[0] == board[3] == board[6] != "-"
  coloum_2 = board[1] == board[4] == board[7] != "-"
  coloum_3 = board[2] == board[5] == board[8] != "-"
  #if there is win we are stopping the while loop
  if coloum_1 or coloum_2 or coloum_3:
    game_continue = False
  if coloum_1:
    return board[0]
  if coloum_2:
    return board[1]
  if coloum_3:
    return board[2]
  return

def check_diagonal():
  global game_continue
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[6] == board[4] == board[2] != "-"
  #if there is win we are stopping the while loop
  if diagonal_1 or diagonal_2:
    game_continue = False
  if diagonal_1:
    return board[0]
  if diagonal_2:
    return board[6]
  return  

def check_tie():
  global game_continue
  if "-" not in board:
    game_continue = False
  return

def flip_player():
  global present_player
  if present_player == "X":
    present_player = "O"
  elif present_player == "O":
    present_player = "X"
  return


play_ttt()










