# Next Greater Element

"""
The next greater element of some element x in an array is the first greater element that is to the right
of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater
element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.
"""

# Runtime: 26ms (Beats 82.83% of users with Python)
# Memory: 13.3MB (Beats 89.6% of users with Python)

from typing import List

class Solution(object):
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Create a hashmap to store the values and indices  
        hashmap: dict[int, int] = {value: index for index, value in enumerate(nums1)}
        # Create a list with -1 to save the result
        result: List[int] = [-1] * len(nums1)

        stack: List[int] = []
        for i in range(len(nums2)):
            current: int = nums2[i]
            
            # Check if the stack isn't empty and if the current value is greater than the last position in the stack  
            while stack and current > stack[-1]:
                # Search hashmap for the index of the last value added to the stack and save in said index but as a result the value of current  
                result[hashmap[stack.pop()]]: int = current
            
            # Add values to the stack if it exists in the hashmap
            if current in hashmap:
                stack.append(current)

        return result 

if __name__ == "__main__":
    solution = Solution()

    s1 = solution.nextGreaterElement([4,1,2],[1,3,4,2])
    s2 = solution.nextGreaterElement([2,4],[1,2,3,4])

    print(s1, s2)

