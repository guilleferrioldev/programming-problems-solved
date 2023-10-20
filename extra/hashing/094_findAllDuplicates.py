# Find all duplicate elements in a limited range array

"""
Find the duplicate numbers in an integer array of size n that contains elements between 1 and n, at least one of which repeats.
"""

from typing import List
from collections import Counter

class Solution:
    def findDuplicates(self, nums: List[int]) -> set[int]:
        # create an empty map to store the count of each array element
        freq: dict[int, int] = {}
 
        # traverse the input array and update the frequency of each element
        for i in nums:
            freq[i]: int = freq.setdefault(i, 0) + 1
 
        # iterate through the frequency map and collect elements having a count of two or more
        return {key for key in freq.keys() if freq[key] >= 2}
 
 
class Solution2:
    def findDuplicates(self, nums: List[int]) -> set[int]:

        return {key for key, value in Counter(nums).items() if value >= 2}


if __name__ == '__main__':
    solution = Solution()
    solution2 = Solution2()
    
    s1 = solution.findDuplicates([5, 3, 4, 2, 5, 1, 2])
    s2 = solution2.findDuplicates([4, 1, 5, 3, 4, 2, 3])

    print(s1, s2)



