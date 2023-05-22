board = {1:"   ", 2:"   ", 3:"   ", 4:"   ", 5:"   ", 6:"   ", 7:"   ", 8:"   ", 9:"   "}

def display():
  print(board[1]+"|"+board[2]+"|"+board[3])
  print("---+---+---")
  print(board[4]+"|"+board[5]+"|"+board[6])
  print("---+---+---")
  print(board[7]+"|"+board[8]+"|"+board[9])

def checkForDraw():
  for i in board.keys():
    if board[i] == "   ": 
      return False
  return True
      
def checkForwin(player):
  if board[1]==board[2]==board[3] == player:
      return True
  elif board[4]==board[5]==board[6] == player:
    return True
  elif board[7]==board[8]==board[9] == player:
    return True
  elif board[1]==board[4]==board[7] == player:
    return True
  elif board[2]==board[5]==board[8] == player:
    return True
  elif board[3]==board[6]==board[9] == player:
    return True
  elif board[1]==board[5]==board[9] == player:
    return True
  elif board[3]==board[5]==board[7] == player:
    return True
  else:
    return False

def isEmpty(position):
  return board[position] == "   "

player = " X "

while True:
  display()
  position = int(input(f"Enter a Position(1-9) for {player}: "))


  if isEmpty(position):
    board[position]= player
    display()
    if checkForwin(player):
      print(player, "is the winner")
      break
    elif checkForDraw():
      print("Game Draw")
      break
  else:
    print("Position Occupied. Enter a New position: ")
    continue
  
  # swapping turns
  if player==" X ":
    player = " O "
  else:
    player = " X "