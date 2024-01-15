# Find the Difference of Two Arrays

"""
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

    answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
    answer[1] is a list of all distinct integers in nums2 which are not present in nums1.

Note that the integers in the lists may be returned in any order.
"""

# Runtime: 127ms (Beats 82.33% of users with Python)
# Memory: 13.67MB (Beats 71.16% of users with Python)

from typing import List

class Solution(object):
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [list(set(nums1).difference(nums2)), list(set(nums2).difference(nums1))]
    
if __name__ == "__main__":
    solution = Solution()
    
    s1 = solution.findDifference([1,2,3], [2,4,6])
    s2 = solution.findDifference([1,2,3,3], [1,1,2,2])
    
    print(s1, s2)