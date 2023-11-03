def is_valid(board, num, row, col):
    n = len(board)

    # Check row
    for r in range(n):
        if board[r][col] == num:
            return False
    
    # Check column
    for c in range(n):
        if board[row][c] == num:
            return False
    
    # Check subgrid (block)
    block_size = int(n ** 0.5)
    block_row = (row // block_size) * block_size
    block_col = (col // block_size) * block_size
    for i in range(block_size):
        for j in range(block_size):
            if board[block_row + i][block_col + j] == num:
                return False
    
    return True

def solve_sudoku(board):
    n = len(board)

    def solve(row, col):
        if row == n:
            return True

        next_row = row + 1 if col == n - 1 else row
        next_col = 0 if col == n - 1 else col + 1

        if board[row][col] > 0:
            return solve(next_row, next_col)

        for num in range(1, n + 1):
            if is_valid(board, num, row, col):
                board[row][col] = num
                if solve(next_row, next_col):
                    return True
                board[row][col] = 0

        return False

    if solve(0, 0):
        return board
    else:
        return None
    
def main(board):
    solution = solve_sudoku(board)
    if solution is not None:
        for row in solution:
            print(row)
    else:
        print("no solution found")


if __name__ == "__main__":
    board = [
    [0, 2, 0, 0],
    [0, 0, 0, 2],
    [3, 0, 0, 0],
    [0, 0, 1, 0]]
    
    main(board)
    
    grid = [[0, 0, 0, 0, 0, 0, 6, 8, 0],
        [0, 0, 0, 0, 7, 3, 0, 0, 9],
        [3, 0, 9, 0, 0, 0, 0, 4, 5],
        [4, 9, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 3, 0, 5, 0, 9, 0, 2],
        [0, 0, 0, 0, 0, 0, 0, 3, 6],
        [9, 6, 0, 0, 0, 0, 3, 0, 8],
        [7, 0, 0, 6, 8, 0, 0, 0, 0],
        [0, 2, 8, 0, 0, 0, 0, 0, 0]]
    
    main(grid)