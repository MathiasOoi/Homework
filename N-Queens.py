# Board is a list of columns
def can_place_queen(board, row, col):
    # Check if a queen can be placed on a given row and column on a given board
    # 1. Is it in the same row
    # 2. Is it in the same column
    # 3. Is it in the same diagonal (Delta x = delta y)
    for curr_row, curr_col in enumerate(board):
        if row == curr_row or curr_col == col or abs(row - curr_row) == abs(col - curr_col):
            return False
    return True

def solve(n):
    # Store the positions of the queens as a list of column positions
    queens, solutions, col, row = [],[], 0, 0
    while True:
        while col < n and not can_place_queen(queens, row, col):
            # Finds the next open column index
            # Even if it doesnt fit on the board
            col += 1
        if col < n:
            # If column fits on the board place it on the board
            queens.append(col)
            if row + 1 >= n:
                # If there are n rows then you have a solution
                solutions.append(queens[:])
                queens.pop()
                col = n
            else:
                # If you don't have a solution and your current board is correct
                # Go on to the next row and reset columns index to 0
                row += 1
                col = 0
        if col >= n:
            # If the column index wont fit on the board
            # Every solution after this would be wrong
            # Remove the last element in queens
            # Go back to the previous row
            if row == 0:
                # If you tried all possible combinations return list of solutions
                return solutions
            col = queens.pop() + 1
            # Start again from the column after the one that doesn't work
            row -= 1

def display_queens(queens, n):
    for k, solution in enumerate(queens):
        # Create a 2d matrix representing a board
        board = [["x" for i in range(n)] for j in range(n)]
        for a, b in enumerate(solution):
            board[a][b] = "Q"
        print("Solution:" + str(k+1) + "\n" + "\n".join(s for s in [" ".join(i) for i in board]))


if __name__ == "__main__":
    n = 4
    solutions = solve(n)
    display_queens(solutions, n)

