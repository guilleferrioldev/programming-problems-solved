# Remove Element

"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.

Return k.
"""

# Runtime: 15ms (Beats 72.31% of users with Python)
# Memory: 13.17MB (Beats 73.44% of users with Python)

from typing import List

class Solution(object):
    def removeElement(self, nums: List[int], val: int) -> int:
        # iterate through the arrays only the amount equal to the values that are repeated
        while nums.count(val) != 0:
            # Remove the values
            nums.remove(val)

        return len(nums)

if __name__ == "__main__":
    solution = Solution()

    s1 = solution.removeElement([3,2,2,3],3)
    s2 = solution.removeElement([0,1,2,2,3,0,4,2], 2)
    
    print(s1, s2)
