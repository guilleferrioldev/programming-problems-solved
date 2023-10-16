# Concatenation of Array 

"""
Given an integer array nums of length n, you want to create an array ans of length 2n
where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.
"""

# Runtime: 44ms (Beats 97.77% of users with Python)
# Memory: 13.3MB (Beats 99.15% of users with Python)

from typing import List

class Solution(object):
    def getConcatenation(self, nums: List[int]) -> List[int]:

        return nums + nums

if __name__ == "__main__":
    solution = Solution()

    s1 = solution.getConcatenation([1,2,1])
    s2 = solution.getConcatenation([1,3,2,1])

    print(s1, s2)

