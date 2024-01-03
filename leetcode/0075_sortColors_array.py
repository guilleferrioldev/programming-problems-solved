# Sort Colors

"""
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""

# Runtime: 15ms (Beats 78.24% of users with Python)
# Memory: 13.29MB (Beats 59.81%of users with Python)

from typing import List

class Solution(object):
    def sortColors(self, nums: List[int]) -> List[int]: 
        low = mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        
        return nums
                 
if __name__ == "__main__":
    solution = Solution()
    
    s1 = solution.sortColors([2,0,2,1,1,0])
    s2 = solution.sortColors([2,0,1])
    
    print(s1, s2)