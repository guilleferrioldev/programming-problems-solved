#  Find the Duplicate Number

"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.
"""

# Runtime: 468ms (Beats 73.74% of users with Python)
# Memory: 25MB (Beats 81.29% of users with Python)

from typing import List

class Solution(object):
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd's cycle detection algorithm
        tortoise: int = nums[0]
        hare : int = nums[0]
        while True:
            tortoise: int = nums[tortoise]
            hare: int = nums[nums[hare]]
            if tortoise == hare:
                break 
        
        ptr1: int = nums[0]
        ptr2: int = tortoise 
        while ptr1 != ptr2:
            ptr1: int = nums[ptr1]
            ptr2: int = nums[ptr2]

        return ptr1


class Solution2:
    def findDuplicate(self, nums: List[int]) -> int:

        hashset: set[int] = set()

        for i in nums:
            if i in hashset:
                return i
            hashset.add(i)

if __name__ == "__main__":
    solution = Solution()
    solution2 = Solution()
    
    s1 = solution.findDuplicate([1,3,4,2,2])
    s2 = solution2.findDuplicate([3,1,3,4,2])
    
    print(s1, s2)
