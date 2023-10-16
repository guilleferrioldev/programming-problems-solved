# Valid Sudoku

"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

"""

# Runtime: 56ms (Beats 87.54% of users with Python)
# Memory: 13.4MB (Beats 47.08% of users with Python)

from collections import defaultdict
from typing import List, Tuple

class Solution(object):
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create empty dictionaries to store the values
        rows: dict[str, str] = defaultdict(set)
        cols: dict[str, str] = defaultdict(set)
        squares: dict[Tuple[str, str], str] = defaultdict(set)
        
        # Iterate through every row
        for row in range(9):
            # Iterate through every column
            for col in range(9):
                # Check if the value is equal to .
                if board[row][col] == ".":
                    continue 
                # Check if the value exists in one of those dictionaries,then return False
                if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in squares[(row//3, col//3)]:
                   return False 
                # Store the current value in said dictionaries
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                squares[(row//3, col//3)].add(board[row][col])
        
        return True

if __name__ == "__main__":
    solution = Solution()
    
    board_1 = [["5","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]

    board_2 = [["8","3",".",".","7",".",".",".","."]
            ,["6",".",".","1","9","5",".",".","."]
            ,[".","9","8",".",".",".",".","6","."]
            ,["8",".",".",".","6",".",".",".","3"]
            ,["4",".",".","8",".","3",".",".","1"]
            ,["7",".",".",".","2",".",".",".","6"]
            ,[".","6",".",".",".",".","2","8","."]
            ,[".",".",".","4","1","9",".",".","5"]
            ,[".",".",".",".","8",".",".","7","9"]]

    s1 = solution.isValidSudoku(board_1)
    s2 = solution.isValidSudoku(board_2)
    print(s1, s2)



