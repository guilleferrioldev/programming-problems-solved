# Construct Quad Tree

"""
Given a n * n matrix grid of 0's and 1's only. We want to represent grid with a Quad-Tree.

Return the root of the Quad-Tree representing grid.

A Quad-Tree is a tree data structure in which each internal node has exactly four children.
Besides, each node has two attributes:

We can construct a Quad-Tree from a two-dimensional area using the following steps:
1. If the current grid has the same value (i.e all 1's or all 0's) set isLeaf True and set val to the value of the grid and 
set the four children to Null and stop.
2. If the current grid has different values, set isLeaf to False and set val to any value and divide the current grid into 
four sub-grids as shown in the photo.
3. Recurse for each of the children with the proper sub-grid.
"""

# Runtime: 85ms (Beats 69.77% of users with Python)
# Memory: 15.69MB (Beats 8.14% of users with Python)

"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

from typing import List

class Solution(object):
    def construct(self, grid: List[List[int]]) -> None:
        def dfs(number, row, column):
            allSame = True
            for i in range(number):
                for j in range(number):
                    if grid[row][column] != grid[row + i][column + j]:
                        allSame = False
                        break
                
            if allSame:
                return Node(grid[row][column], True)
            
            number = number // 2
            topLeft = dfs(number, row, column)
            topRight = dfs(number, row, column + number)
            bottomLeft = dfs(number, row + number, column)
            bottomRight = dfs(number, row + number, column + number)
            return Node(0, False, topLeft, topRight, bottomLeft, bottomRight)
            
        return dfs(len(grid), 0, 0)