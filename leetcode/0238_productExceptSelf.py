# Product of Array Except Self

"""
Given an integer array nums, return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

# Runtime: 158ms (Beats 85.21% of users with Python)
# Memory: 20.66MB (Beats 78.25% of users with Python)

from typing import List

class Solution(object):
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result: List[int] = [1] * (len(nums))

        prefix: int =  1 
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        postfix: int =  1 
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result
if __name__ == "__main__":
    solution = Solution()

    s1 = solution.productExceptSelf([1,2,3,4])
    s2 = solution.productExceptSelf([-1,1,0,-3,3])

    print(s1, s2)
