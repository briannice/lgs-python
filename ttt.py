print("Tic Tac Toe")
print("-----------")
print("")


def print_board(board):
    for i in range(0,16,4):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} | {board[i+3]}")
        if i != 12:
            print(f"---------------")
    print("")


board = [" ", "1", "2", "3", "1", " ", " ", " ", "2", " ", " ", " ", "3", " ", " ", " "]
player = 1
winner = False

while not winner:
    print_board(board)

    if player == 1:
        print("Player 1:")
    elif player == 2:
        print("Player 2:")

    row = int(input("Row: "))
    col = int(input("Column: "))
    print("")

    if row < 1 or row > 3:
        print("Row must be between 1 and 3! Try again...")
        print("")
    elif col < 1 or col > 3:
        print("Column must be between 1 and 3! Try again...")
        print("")
    elif board[4 * row + col] != " ":
        print("Cell is already filled! Try again...")
        print("")
    else:
        if player == 1:
            board[4 * row + col] = "X"
        elif player == 2:
            board[4 * row + col] = "O"

        # Check rows
        if board[5] == board[6] and board[5] == board[7] and board[5] != " ":
            if player == 1:
                print("Player 1 win.")
            else:
                print("Player 2 win.")
            winner = True
        
        if board[9] == board[10] and board[9] == board[11] and board[9] != " ":
            if player == 1:
                print("Player 1 win.")
            else:
                print("Player 2 win.")
            winner = True
        
        if board[13] == board[14] and board[13] == board[15] and board[13] != " ":
            if player == 1:
                print("Player 1 win.")
            else:
                print("Player 2 win.")
            winner = True
        
        # Check columns
        if board[5] == board[9] and board[5] == board[13] and board[5] != " ":
            if player == 1:
                print("Player 1 win.")
            else:
                print("Player 2 win.")
            winner = True
        
        if board[6] == board[10] and board[6] == board[14] and board[6] != " ":
            if player == 1:
                print("Player 1 win.")
            else:
                print("Player 2 win.")
            winner = True
        
        if board[7] == board[11] and board[7] == board[15] and board[7] != " ":
            if player == 1:
                print("Player 1 win.")
            else:
                print("Player 2 win.")
            winner = True
        
        # Check diagonals
        if board[5] == board[10] and board[5] == board[15] and board[5] != " ":
            if player == 1:
                print("Player 1 win.")
            else:
                print("Player 2 win.")
            winner = True
        if board[7] == board[10] and board[7] == board[13] and board[7] != " ":
            if player == 1:
                print("Player 1 win.")
            else:
                print("Player 2 win.")
            winner = True
        
        # Tie
        if not winner and board.count(" ") < 1:
            winner = True
            print("It's a tie.")

        if not winner:
            if player == 1:
                player = 2  # player2
            else:
                player = 1  # player1

print_board(board)