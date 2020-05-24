import time
start = time.time()
def can_place_queen(board, row, col):
    # Check if a queen can be placed on a given column and column index on a given board
    # 1. Is it in the same row
    # 2. Is it in the same column
    # 3. Is it in the same diagonal (Delta x = delta y)
    for curr_row, curr_col in enumerate(board):
        if row == curr_row or curr_col == col or abs(row - curr_row) == abs(col - curr_col):
            return False
    return True

def solve(n):
    # Store the positions of the queens as a list of column positions
    queens, solutions, col = [],[], 0,
    while True:
        print(queens)
        while col < n and not can_place_queen(queens, len(queens), col):
            # Finds the next open column index on the next column
            col += 1
            if col >= n:
                break
        if col < n:
            # If column fits on the board place it on the board
            queens.append(col)
            if len(queens) >= n:
                print(queens)
                # If there are n rows then you have a solution
                solutions.append(queens[:])
                queens.pop()
                col = n
            else:
                # If you don't have a solution and your current board is possible
                # Go on to the next column and reset columns index to 0
                col = 0
        if col >= n:
            # If the column index wont fit on the board
            # Solutions down this path will also be wrong
            # So you should stop searching
            # Remove the last element in queens
            # Go back to the previous column
            if not queens:
                # If you tried all possible combinations return list of solutions if there are any
                return solutions
            # Else start again from the same column at the next index
            col = queens.pop() + 1

def display_queens(queens, n):
    if not queens:
        print("No solution")
    else:
        for k, solution in enumerate(queens):
            # Create a 2d matrix representing a board
            board = [["x" for i in range(n)] for j in range(n)]
            for a, b in enumerate(solution):
                board[a][b] = "Q"
            print("Solution:" + str(k+1) + "\n" + "\n".join(s for s in [" ".join(i) for i in board]))


if __name__ == "__main__":
    n = 8
    solutions = solve(n)
    display_queens(solutions, n)
    print(time.time() - start)

