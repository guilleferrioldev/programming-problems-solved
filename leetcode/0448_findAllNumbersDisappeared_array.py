# Find All Numbers Disappeared in an Array

"""
Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.
"""

# Runtime: 24ms (Beats 91.59% of users with Python)
# Memory: 13.6MB (Beats 94.76% of users with Python)

from typing import List

class Solution(object):
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        return list(set(range(1, len(nums) + 1)) - set(nums))

if __name__ == "__main__":
    solution = Solution()

    s1 = solution.findDisappearedNumbers([4,3,2,7,8,2,3,1])
    s2 = solution.findDisappearedNumbers([1,1])

    print(s1, s2)
