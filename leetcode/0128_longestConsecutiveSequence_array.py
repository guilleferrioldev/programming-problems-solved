# Longest Consecutive Sequence

"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

# Runtime: 345ms (Beats 56.88% of users with Python)
# Memory: 30.53MB (Beats 26.99% of users with Python)

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create a set with the values from the list to make sure it doesn't have repeated values 
        hashset: set[int] = set(nums)
        longest: int = 0

        for n in hashset:
            # check if its the start of a sequence
            if (n - 1) not in hashset:
                length: int = 1
                # Continue iterating through the set and add 1 when the next value exists
                while (n + length) in hashset:
                    length += 1
                # Stay with the largest length
                longest: int = max(length, longest)
        
        return longest

if __name__ == "__main__":
    solution = Solution()

    s1 = solution.longestConsecutive([100,4,200,1,3,2])
    s2 = solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1])

    print(s1, s2)
