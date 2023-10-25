# Two Sum II - Input Array Is Sorted

"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that 
they add up to a specific target number.
Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""

# Runtime: 102ms (Beats 82.94% of users with Python)
# Memory: 13.96MB (Beats 24.56% of users with Python)

from typing import List 

class Solution(object):
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # point to the beginning and the end
        start, end = 0, len(numbers) -1 
        
        # Iterate until the two pointers match
        while start < end:
            # Add the current positions
            curSum = numbers[start] + numbers[end]
            
            # If the sum is equal to the target return the positions plus 1
            if curSum == target:
                 return [start + 1, end + 1]
            # If the sum is greater than the target, increase the position of the start pointer
            elif curSum < target:
                start += 1 
            # If the sum is less than the target, decrease the position of the end pointer
            else:
               end -= 1

if __name__ == "__main__":
    solution = Solution()

    s1 = solution.twoSum([2,7,11,15], 9)
    s2 = solution.twoSum([2,3,4], 6)
    s3 = solution.twoSum([-1, 0], -1)

    print(s1, s2, s3)

