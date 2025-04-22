def is_safe(board, row, col):
    # Check if it is safe to place a queen at the given position

    # Check the row
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal
    i, j = row, col
    while i < 8 and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def solve_queens(board, col):
    # Base case: If all queens are placed, return True
    if col >= 8:
        return True

    # Recursive case: Try placing the queen in each row of the current column
    for i in range(8):
        if is_safe(board, i, col):
            # Place the queen
            board[i][col] = 1

            # Recursive call to place the remaining queens
            if solve_queens(board, col + 1):
                return True

            # Backtrack and remove the queen from the current position
            board[i][col] = 0

    # If no solution is found, return False
    return False


def print_solution(board):
    # Print the board
    for i in range(8):
        for j in range(8):
            print(board[i][j], end=' ')
        print()


def solve_8_queens():
    # Create an empty 8x8 chessboard
    board = [[0 for _ in range(8)] for _ in range(8)]

    # Solve the 8 Queens problem
    if solve_queens(board, 0):
        print("Solution exists:")
        print_solution(board)
    else:
        print("No solution exists.")


# Run the solver
solve_8_queens()
