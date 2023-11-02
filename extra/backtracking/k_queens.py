def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []

    def is_safe(row, col):
        # Check column
        for r in range(row):
            if board[r][col] == 1:
                return False
        
        # Check upper left diagonal
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1
        
        # Check upper right diagonal
        i, j = row, col
        while i >= 0 and j < n:
            if board[i][j] == 1:
                return False
            i -= 1
            j += 1
        
        return True

    def solve(row):
        if row == n:
            #We found a solution
            solution = []
            for i in range(n):
                row = []
                for j in range(n):
                    if board[i][j] == 1:
                        row.append(' Q ')
                    else:
                        row.append(' x ')
                solution.append(''.join(row))
            solutions.append(solution)
        else:
            for col in range(n):
                if is_safe(row, col):
                    board[row][col] = 1
                    solve(row + 1)
                    board[row][col] = 0

    #We call the resolve function with the first row resolve(0) 
    solve(0)

    return solutions


def main(n):
    solutions = solve_n_queens(n)
    for i, solution in enumerate(solutions):
        print(f"Solución {i + 1}:")
        for row in solution:
            print(row)
        print()

if __name__ == "__main__":
    n = 8
    main(n)

