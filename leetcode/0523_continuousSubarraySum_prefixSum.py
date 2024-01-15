# Continuous Subarray Sum

"""
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

    its length is at least two, and
    the sum of the elements of the subarray is a multiple of k.

Note that:

    A subarray is a contiguous part of the array.
    An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
"""

# Runtime: 847ms (Beats 97.31% of users with Python)
# Memory: 33.16MB (Beats 61.83% of users with Python)

from typing import List

class Solution(object):
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0: -1}
        total = 0

        for index, num in enumerate(nums):
            total += num
            rem = total % k
            if rem not in remainder:
                remainder[rem] = index
            elif index - remainder[rem] > 1:
                return True
        return False
    
if __name__ == "__main__":
    solution = Solution()
    
    s1 = solution.checkSubarraySum([23,2,4,6,7], 6)
    s2 = solution.checkSubarraySum([23,2,6,4,7], 6)
    s3 = solution.checkSubarraySum([23,2,6,4,7], 13)
    
    print(s1, s2, s3)