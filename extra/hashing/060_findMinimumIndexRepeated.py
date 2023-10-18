# Find the minimum index of a repeating element in an array

"""
Given an integer array, find the minimum index of a repeating element in linear time
and doing just a single traversal of the array.
"""

from typing import List
from collections import Counter

class Solution:
    def findMinIndex(self, nums: List[int]) -> int:
        minIndex = -1
        # create an empty set to store list elements
        s = set()
 
        # traverse the list from right to left
        for index in reversed(range(len(nums))): 
            # if the element is seen before, update the minimum index
            if nums[index] in s:
                minIndex = index
            # if the element is seen for the first time, insert it into the set
            s.add(nums[index])
        
        return minIndex

if __name__ == "__main__":
    solution = Solution()

    s1 = solution.findMinIndex([5, 6, 3, 4, 3, 6, 4])
    s2 = solution.findMinIndex([1, 2, 3, 4, 5, 6])

    print(s1, s2)
    
