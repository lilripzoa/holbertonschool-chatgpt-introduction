def print_board(board):
    # Print each row with " | " separator and a line between rows
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows for winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonal (top-left to bottom-right) for winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    # Check diagonal (top-right to bottom-left) for winner
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def valid_input():
    # Validate that the input is an integer between 0 and 2
    while True:
        try:
            value = int(input("Enter a value (0, 1, or 2): "))
            if value in [0, 1, 2]:
                return value
            else:
                print("Invalid input. Please enter a number between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def tic_tac_toe():
    # Initialize the board and set the first player as "X"
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    # Loop until there is a winner
    while not check_winner(board):
        print_board(board)
        
        # Get valid row and column input from the current player
        print(f"Player {player}'s turn:")
        
        row = valid_input()
        col = valid_input()
        
        # Check if the chosen spot is available
        if board[row][col] == " ":
            board[row][col] = player
            # Switch players after a valid move
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

    print_board(board)
    # The player who just moved (aft
