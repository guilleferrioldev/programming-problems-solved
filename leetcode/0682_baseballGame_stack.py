# Baseball Game

"""
You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

    An integer x.
        Record a new score of x.
    '+'.
        Record a new score that is the sum of the previous two scores.
    'D'.
        Record a new score that is the double of the previous score.
    'C'.
        Invalidate the previous score, removing it from the record.

Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.
"""

# Runtime: 21ms (Beats 66.15% of users with Python)
# Memory: 13.8MB (Beats 39.83% of users with Python)

from typing import List

class Solution(object):
    def calPoints(self, operations: List[str]) -> int:
        stack: List[int] = []

        for element in operations:            
            if element == "C":
                stack.pop()
            elif element == "D" :
                double = stack[-1]
                stack.append(2 * double)
            elif element == "+":
                sum1 = stack[-2:]
                stack.append(sum(sum1))
            else:
                stack.append(int(element))
        
        return sum(stack)
        
if __name__ == "__main__":
    solution = Solution()
    s1 = solution.calPoints(["5","2","C","D","+"])
    s2 = solution.calPoints(["5","-2","4","C","D","9","+","+"])
    s3 = solution.calPoints(["1","C"])
    
    print(s1, s2, s3)