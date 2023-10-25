# Rotate Array

"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""

# Runtime: 153ms (Beats 55.95% of users with Python)
# Memory: 24.67MB (Beats 89.04% of users with Python)

from typing import List

class Solution(object):
    def rotate(self, nums: List[int], k: int) -> None:
        k: int = k % len(nums)
        
        # Swap the k positions with the -k ones [:k] <=> [-k:]
        start , end = 0, len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
        
        # Sort the first positions [:k]
        first, middle_end = 0, k - 1
        while first < middle_end:
            nums[first], nums[middle_end] = nums[middle_end], nums[first]
            first, middle_end = first + 1, middle_end - 1
        
        # Sort the latest positions
        middle_start, end = k, len(nums) - 1
        while middle_start < end:
            nums[middle_start], nums[end] = nums[end], nums[middle_start]
            middle_start, end = middle_start + 1, end - 1

if __name__ == "__main__":
    solution = Solution()

    s1 = solution.rotate([1,2,3,4,5,6,7], 3)
    s2 = solution.rotate([-1,-100,3,99], 2)
    s3 = solution.rotate([-1], 2)
    s4 = solution.rotate([1], 0)
