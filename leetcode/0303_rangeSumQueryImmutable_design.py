#  Range Sum Query - Immutable

"""
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

"""

# Runtime: 370ms (Beats 46.58% of users with Python)
# Memory: 16.75MB (Beats 90.98% of users with Python)

from typing import List

class NumArray(object):
    def __init__(self, nums: List[int]) -> None:
    
        self.nums: List[int] = nums 

    def sumRange(self, left: int, right: int) -> int:
        
        return sum(self.nums[left: right+1])


if __name__ == "__main__":
    solution = NumArray([-2, 0, 3, -5, 2, -1])

    s1 = solution.sumRange(0,2)
    s2 = solution.sumRange(2,5)
    s3 = solution.sumRange(0,5)
    
    print(s1, s2, s3)
