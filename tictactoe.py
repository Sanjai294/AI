import math

# Initialize the board
board = [' ' for _ in range(9)]

# Print the board
def print_board():
    for i in range(3):
        print(board[3*i] + ' | ' + board[3*i+1] + ' | ' + board[3*i+2])
        if i < 2:
            print('---------')

# Check for winner
def winner(b, player):
    win_cond = [(0,1,2), (3,4,5), (6,7,8),
                (0,3,6), (1,4,7), (2,5,8),
                (0,4,8), (2,4,6)]
    for x, y, z in win_cond:
        if b[x] == b[y] == b[z] == player:
            return True
    return False

# Check for draw
def is_draw():
    return ' ' not in board

# Get available moves
def available_moves(b):
    return [i for i in range(9) if b[i] == ' ']

# Minimax algorithm
def minimax(b, depth, is_maximizing):
    if winner(b, 'O'):
        return 1
    elif winner(b, 'X'):
        return -1
    elif is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in available_moves(b):
            b[i] = 'O'
            score = minimax(b, depth + 1, False)
            b[i] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in available_moves(b):
            b[i] = 'X'
            score = minimax(b, depth + 1, True)
            b[i] = ' '
            best_score = min(score, best_score)
        return best_score

# AI move
def ai_move():
    best_score = -math.inf
    move = None
    for i in available_moves(board):
        board[i] = 'O'
        score = minimax(board, 0, False)
        board[i] = ' '
        if score > best_score:
            best_score = score
            move = i
    board[move] = 'O'

# Play the game
def play_game():
    print("Welcome to Tic Tac Toe!")
    print_board()

    while True:
        # Player move
        move = int(input("Enter your move (0-8): "))
        if board[move] != ' ':
            print("Invalid move. Try again.")
            continue
        board[move] = 'X'
        print_board()

        if winner(board, 'X'):
            print("You win!")
            break
        elif is_draw():
            print("It's a draw!")
            break

        # AI move
        print("AI is thinking...")
        ai_move()
        print_board()

        if winner(board, 'O'):
            print("AI wins!")
            break
        elif is_draw():
            print("It's a draw!")
            break

# Run the game
if __name__ == "__main__":
    play_game()
