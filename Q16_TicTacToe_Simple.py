# Code by Lightning Monster❤️
"""
Q.16) Write a Python program to solve Tic-Tac-Toe problem.
[20 Marks]

Description:
A simple 2-player Tic-Tac-Toe (X vs O) game on a 3x3 board.
Players take turns, the program checks for win/draw after each move.
"""

# Function to print the board
def print_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

# Function to check if someone has won
def check_winner(board, mark):
    win_combinations = [
        (0,1,2), (3,4,5), (6,7,8),     # rows
        (0,3,6), (1,4,7), (2,5,8),     # columns
        (0,4,8), (2,4,6)               # diagonals
    ]

    for a, b, c in win_combinations:
        if board[a] == board[b] == board[c] == mark:
            return True
    return False

# Function to check if the board is full
def is_draw(board):
    return all(cell != " " for cell in board)

# Main Program
def main():
    board = [" "] * 9
    current_player = "X"

    print("🎮 Simple Tic-Tac-Toe")
    print("Positions:")
    print("1 | 2 | 3")
    print("--+---+--")
    print("4 | 5 | 6")
    print("--+---+--")
    print("7 | 8 | 9")

    while True:
        print_board(board)

        try:
            move = int(input(f"Player {current_player}, enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid position! Choose between 1 and 9.")
                continue
        except ValueError:
            print("Enter a valid number.")
            continue

        idx = move - 1

        # Check if spot is free
        if board[idx] != " ":
            print("Spot already taken! Try again.")
            continue

        # Place the marker
        board[idx] = current_player

        # Check winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"🏆 Player {current_player} wins!")
            break

        # Check draw
        if is_draw(board):
            print_board(board)
            print("🤝 It's a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
