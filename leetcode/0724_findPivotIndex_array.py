# Fivot Index

"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left 
of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are
no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.
"""

# Runtime: 87ms (Beats 99.77% of users with Python)
# Memory: 14.31MB (Beats 55.58% of users with Python)

from typing import List

class Solution(object):
    def pivotIndex(self, nums: List[int]) -> int:
        
        left_sum: int  = 0
        total_sum : int = sum(nums)

        for index, num in enumerate(nums):
            if left_sum == (total_sum - left_sum - num):
                return index
            
            left_sum += num

        return -1                

if __name__ == "__main__":
    solution = Solution()

    s1 = solution.pivotIndex([1,7,3,6,5,6])
    s2 = solution.pivotIndex([1,2,3])
    s3 = solution.pivotIndex([2,1,-1])

    print(s1, s2, s3)

