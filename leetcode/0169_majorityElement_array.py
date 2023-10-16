# Majority Element

"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.
"""

# Runtime: 120ms (Beats 60.81% of users with Python)
# Memory: 14.59MB (Beats 92.05% of users with Python)

from typing import List 

class Solution(object):
    def majorityElement(self, nums: List[int]) -> int:
        # Sort the array and return the middle position
        return sorted(nums)[len(nums) / 2]

