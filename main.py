import random  # 🎲 Importing random for computer bot's move

# 🌟 GLOBAL VARIABLES
game_board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]  # 🛑 Initial empty board
current_player = "X"  # ❌ Player X starts first
winner = None  # 🏆 No winner yet
game_on = True  # 🔄 The game is running

# 🎨 ASCII Art: Welcome Message
print(r"""
  _____   _         _____   _____   _____           _____    ____  
 |_   _| | |       |_   _| |  ___| |  _  |         |  _  |  /  __| 
   | |   | |__       | |   | |___  | |_| |  ____   | |_| |  | |__  
   | |   | '_ \      | |   |  ___| |  _  / |____|  |  _  /  \___ \ 
   | |   | | | |    _| |_  | |___  | | \ \         | | \ \   ___| | 
   |_|   |_| |_|   |_____| |_____| |_|  \_\        |_|  \_\ |_____/ 

""")


# 🖥️ PRINT THE BOARD
def display_board(board):
    # Display the current state of the board with grid layout
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-" * 10)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-" * 10)
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")


# 📝 TAKE USER INPUT
def player_input(board):
    while True:  # Loop until the player makes a valid move
        # Ask the player to choose a position
        position = int(input("Choose the position (1-9): "))
        if position >= 1 and position <= 9:  # Check if the input is valid
            if board[position - 1] == "-":  # Check if the spot is free
                board[position - 1] = current_player  # Place the player's mark
                break  # Exit the loop after a valid move
            else:
                display_board(board)
                print("⚠️ Oops! Spot already full, try again! 🙁")  # Spot taken
        else:
            display_board(board)
            print("🚫 Invalid input! Please enter a number between 1 and 9. 🚫")


# 🏆 CHECK FOR WIN OR TIE
def check_horizontal(board):
    global winner
    # Check all horizontal rows for a win
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]  # Set the winner
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    return False


def check_vertically(board):
    global winner
    # Check all vertical columns for a win
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    return False


def check_diagonals(board):
    global winner
    # Check both diagonals for a win
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True
    return False


def check_tie(board):
    global game_on
    if "-" not in board:  # Check if the board is full (tie condition)
        display_board(board)
        print("🤝 It's a TIE! 🤝")
        game_on = False


def switch_player():
    global current_player
    # Switch the current player between "X" and "O"
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def check_win(board):
    global game_on
    # Check if any win condition is met
    if check_horizontal(board) or check_vertically(board) or check_diagonals(board):
        display_board(board)
        print(f"🎉 The winner is {winner}! 🎉")
        game_on = False


def computer_bot(board):
    while current_player == "O":  # Only move for player "O"
        position = random.randint(0, 8)  # Choose a random position
        if board[position] == "-":  # If the spot is free, place "O"
            board[position] = "O"
            switch_player()  # Switch back to player "X"


# 🎮 MAIN GAME LOOP
while game_on:
    display_board(board=game_board)  # Show the current board
    player_input(board=game_board)  # Player X makes a move
    check_win(board=game_board)  # Check if player X won
    if game_on:  # If the game hasn't ended
        check_tie(board=game_board)  # Check for a tie
        switch_player()  # Switch to player O
        computer_bot(board=game_board)  # Computer bot makes a move for "O"
        check_win(game_board)  # Check if player O won
        check_tie(game_board)  # Check for a tie again
