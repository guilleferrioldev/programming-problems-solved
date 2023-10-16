# Brick Wall

"""
There is a rectangular brick wall in front of you with n rows of bricks. The ith row has some number 
of bricks each of the same height (i.e., one unit) but they can be of different widths.
The total width of each row is the same.

Draw a vertical line from the top to the bottom and cross the least bricks. If your line goes through
the edge of a brick, then the brick is not considered as crossed. You cannot draw a line just along one
of the two vertical edges of the wall, in which case the line will obviously cross no bricks.

Given the 2D array wall that contains the information about the wall, return the minimum number of 
crossed bricks after drawing such a vertical line.
"""

from typing import List

class Solution(object):
    def leastBricks(self, walls: List[List[int]]) -> int:
        # Hashmap to save count all values
        countGap: dict[int, int] = {0 : 0}
        
        for wall in walls:
            # Variable to initialize the sum of the values on each wall
            sum_counter: int = 0
            for brick in wall[:-1]:
                # Accumulate each value
                sum_counter += brick
                # Save the value in the hashmap
                countGap[sum_counter]: int = countGap.get(sum_counter, 0) + 1
        
        # Subtract the maximum number of gaps from the number of walls
        return len(walls) - max(countGap.values())
                
if __name__ == "__main__":
    solution = Solution()

    s1 = solution.leastBricks([[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]])
    s2 = solution.leastBricks([[1],[1],[1]])
    
    print(s1, s2)



