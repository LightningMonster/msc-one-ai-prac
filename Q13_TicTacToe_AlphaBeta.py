# Code by Lightning Monster❤️
"""
Q.13) Write a Python program to implement Tic-Tac-Toe using Alpha-Beta Pruning.
[20 Marks]

Description:
- Human vs AI on a 3x3 board.
- AI uses Minimax with Alpha-Beta pruning to play optimally.
- Human can choose mark (X/O) and who plays first.
"""

import math

HUMAN, AI = None, None  # will be set based on user choice
EMPTY = " "

def print_board(board):
    print("\n")
    for r in range(3):
        row = " | ".join(board[r*3:(r+1)*3])
        print(f" {row} ")
        if r < 2:
            print("---+---+---")
    print("\n")

def winner(board):
    wins = [
        (0,1,2), (3,4,5), (6,7,8),       # rows
        (0,3,6), (1,4,7), (2,5,8),       # cols
        (0,4,8), (2,4,6)                 # diags
    ]
    for a,b,c in wins:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    return None

def is_full(board):
    return all(cell != EMPTY for cell in board)

def game_over(board):
    return winner(board) is not None or is_full(board)

def evaluate(board, depth):
    w = winner(board)
    if w == AI:
        # prefer faster wins (bigger score with smaller depth)
        return 10 - depth
    elif w == HUMAN:
        # prefer slower losses (less negative with greater depth)
        return depth - 10
    return 0  # draw / non-terminal for eval at leaves

def minimax(board, depth, alpha, beta, maximizing):
    if game_over(board):
        return evaluate(board, depth), None

    best_move = None
    if maximizing:
        value = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                score, _ = minimax(board, depth + 1, alpha, beta, False)
                board[i] = EMPTY
                if score > value:
                    value, best_move = score, i
                alpha = max(alpha, value)
                if alpha >= beta:
                    break  # alpha-beta prune
        return value, best_move
    else:
        value = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                score, _ = minimax(board, depth + 1, alpha, beta, True)
                board[i] = EMPTY
                if score < value:
                    value, best_move = score, i
                beta = max(-math.inf, min(beta, value))
                if alpha >= beta:
                    break  # alpha-beta prune
        return value, best_move

def ai_move(board):
    _, move = minimax(board, 0, -math.inf, math.inf, True)
    return move

def human_move(board):
    while True:
        try:
            pos = int(input("Enter your move (1-9): "))
            if pos < 1 or pos > 9:
                print("Choose a number between 1 and 9.")
                continue
            idx = pos - 1
            if board[idx] != EMPTY:
                print("That cell is already taken. Try again.")
                continue
            return idx
        except ValueError:
            print("Please enter a valid integer from 1 to 9.")

def main():
    global HUMAN, AI

    # Setup
    while True:
        choice = input("Choose your mark (X/O): ").strip().upper()
        if choice in {"X", "O"}:
            HUMAN = choice
            AI = "O" if HUMAN == "X" else "X"
            break
        print("Please type X or O.")

    first = input("Do you want to play first? (y/n): ").strip().lower() == "y"

    board = [EMPTY] * 9
    print("\nPositions reference:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print("\nGame start!")

    turn = HUMAN if first else AI
    while not game_over(board):
        print_board(board)
        if turn == HUMAN:
            idx = human_move(board)
            board[idx] = HUMAN
            turn = AI
        else:
            print("AI is thinking...")
            idx = ai_move(board)
            board[idx] = AI
            turn = HUMAN

    print_board(board)
    w = winner(board)
    if w is None:
        print("It's a draw!")
    elif w == HUMAN:
        print("You win! 🎉")
    else:
        print("AI wins! 🤖")

if __name__ == "__main__":
    main()
