# Remove Duplicates from Sorted Array 

"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that
each unique element appears only once. The relative order of the elements should be kept the same.
Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they
were present in nums initially. The remaining elements of nums are not important as well as the size of nums.

Return k.
"""

# Runtime: 57ms (Beats 66.53% of users with Python)
# Memory: 14.9MB (Beats 20.79% of users with Python)

from typing import List

class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        # Variable to move numbers towards that position
        left = 1
        
        for pos in range(1, len(nums)):
            # If the number in the current position is different from the number in the previous position
            if nums[pos] != nums[pos - 1]:
                # Move the number
                nums[left] =  nums[pos]
                # Increase moving position 
                left += 1
        
        return left


if __name__ == "__main__":
    solution = Solution()

    s1 = solution.removeDuplicates([1,1,2])
    s2 = solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4])

    print(s1, s2)
    

