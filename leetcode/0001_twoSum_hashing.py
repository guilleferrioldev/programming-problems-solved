# Two Sum

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

# Runtime: 40ms (Beats 70.64% of users with Python)
# Memory: 14MB (Beats 78.52% of users with Python)

from typing import List

class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int] | None:
        # Hashmap to save all diff values   
        hashmap: dict[int, int] = dict()

        for index , value in enumerate(nums):
            # Difference between the target and the current value
            diff: int = target - value 
            # Check if the value is in the hasmap, then return the positions
            if diff in hashmap:
                return [hashmap[diff], index]
            # Save the value in the hashmap
            hashmap[value] = index 
        
        return 


if __name__ == "__main__":
    solution = Solution()

    s1 = solution.twoSum([2,7,11,15], 9)
    s2 = solution.twoSum([3,2,4], 6)
    s3 = solution.twoSum([3,3], 6)

    print(s1, s2, s3)
