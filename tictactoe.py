import random


board = [" - ", " - ", " - ",
         " - ", " - ", " - ",
         " - ", " - ", " - ",]

current_player = " X "
winner = None
game_running = True
#printing the game board
def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----------")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----------")
    print(board[6] + "|" + board[7] + "|" + board[8])


#take player imput
def player_input(board):
    inp = int(input("enter a number 1-9 "))
    if inp >=1 and inp<=9 and board[inp-1] == " - ":
        board[inp-1]=current_player
    else:
        print("opps player is already in that spot!")
#check for win or tie
def check_horizontalwin(board):
    global winner
    if board[0]==board[1]==board[2] and board[1]!= " - ":
        winner = board[0]
        return True
    elif board[3] ==board[4] == board [5] and board[3] != " - ":
        winner = board[3]
        return True 
    elif board[6] ==board[7] ==board[8] and board[6] != " - ":
        winner = board[6]
        return True
    
def checkRow_win(board):
    global winner
    if board[0] == board[3]==board[6] and board[0] !=" - ":
        winner= board[3]
        return True
    elif board[1]== board[4]==board[7] and board[1] != " - ":
        winner = board [1]
        return True
    elif board[2]== board[5]==board[8] and board[2] != " - ":
        winner = board [2]
        return True

def checkDiagonal_win(board):
    global winner
    if board[0] == board[4]==board[8] and board[0] !=" - ":
        winner= board[0]
        return True
    elif board[2] == board[4]==board[6] and board[2] !=" - ":
        winner= board[2]
        return True
def checkTie(board):
    global game_running
    if " - " not in board:
        print_board(board)
        print("It is a tie!")
        game_running = False

def checkWin():
    if check_horizontalwin(board) or checkRow_win(board) or checkDiagonal_win(board):
        print(f"the winner is {winner}")
#switch player
def switch_player():
    global current_player
    if current_player ==" X ":
        current_player = " O "
    else:
        current_player = " X "

# computer
def computer(board):
    while current_player == " O ":
        position = random.randint(0, 8)
        if board[position] ==" - ":
            board[position] = " O "
            switch_player()


#check for win or tie again
while game_running:
    print_board(board)
    player_input(board)
    checkWin()
    checkTie(board)
    switch_player()
    computer(board)
    checkWin()
    checkTie(board)

 
  