import math

def evaluate(board):
    # Check rows
    for row in board:
        if len(set(row)) == 1 and row[0] != 0:
            return row[0]

    # Check columns
    for col in range(3):
        if len(set([board[row][col] for row in range(3)])) == 1 and board[0][col] != 0:
            return board[0][col]

    # Check diagonals
    if len(set([board[i][i] for i in range(3)])) == 1 and board[0][0] != 0:
        return board[0][0]

    if len(set([board[i][2 - i] for i in range(3)])) == 1 and board[0][2] != 0:
        return board[0][2]

    # No winner
    return 0

def is_board_full(board):
    for row in board:
        if 0 in row:
            return False
    return True

def minimax(board, depth, is_maximizing_player):
    score = evaluate(board)

    if score != 0:
        return score - depth  # Favor faster wins and slower losses

    if is_board_full(board):
        return 0

    if is_maximizing_player:
        best_score = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == 0:
                    board[row][col] = 1
                    score = minimax(board, depth + 1, False)
                    board[row][col] = 0
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == 0:
                    board[row][col] = -1
                    score = minimax(board, depth + 1, True)
                    board[row][col] = 0
                    best_score = min(best_score, score)
        return best_score

def find_best_move(board):
    best_score = -math.inf
    best_move = None

    for row in range(3):
        for col in range(3):
            if board[row][col] == 0:
                board[row][col] = 1
                score = minimax(board, 0, False)
                board[row][col] = 0

                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    return best_move

def print_board(board):
    symbols = {1: 'X', -1: 'O', 0: '.'}
    for row in board:
        print(" ".join(symbols[cell] for cell in row))
    print()

def play_game():
    board = [[0, 0, 0] for _ in range(3)]
    current_player = 1  # 1: Human (X), -1: AI (O)

    while True:
        print_board(board)

        if current_player == 1:
            print("Player X's turn")
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
                if board[row][col] != 0:
                    print("Invalid move! Try again.")
                    continue
            except (ValueError, IndexError):
                print("Invalid input! Try again.")
                continue
            board[row][col] = 1
        else:
            print("Player O's turn (AI is thinking...)")
            best_move = find_best_move(board)
            if best_move:
                row, col = best_move
                board[row][col] = -1
            else:
                print("No valid moves left.")
                break

        winner = evaluate(board)

        if winner != 0:
            print_board(board)
            if winner == 1:
                print("Player X wins!")
            else:
                print("Player O wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player *= -1

play_game()
