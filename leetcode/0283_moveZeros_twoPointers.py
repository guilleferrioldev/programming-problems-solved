# Move Zeros

"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

# Runtime: 121ms (Beats 94.35% of users with Python)
# Memory: 20.8MB (Beats 80.8% of users with Python)

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Variable to mark the first position
        marker: int = 0

        for pos in range(len(nums)):
            # if the current position is other than 0 and the marker is equal to 0
            if nums[pos] != 0 and nums[marker] == 0:
                # the marker position is exchanged for the current one
                nums[marker], nums[pos] = nums[pos], nums[marker]
            
            # increase the position of the marker if it is not equal to zero
            if nums[marker] != 0:
                marker += 1

if __name__ == "__main__":
    solution = Solution()

    s1 = solution.moveZeroes([0,1,0,3,12]))
    s2 = solution.moveZeroes([0])

