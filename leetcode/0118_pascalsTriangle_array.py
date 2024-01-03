# 118 Pascal's Triangle

"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown
"""

# Runtime: 14ms (Beats 77.39% of users with Python)
# Memory: 13.28MB (Beats 59.56% of users with Python)

from typing import List

class Solution(object):
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
        
        res = [[1]]

        for i in range(numRows -1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j+1])

            res.append(row)

        return res
    
if __name__ == "__main__":
    solution = Solution()
    
    s1 = solution.generate(5)
    s2 = solution.generate(1)
    
    print(s1, s2)