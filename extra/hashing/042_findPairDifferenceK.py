# Find pairs with difference k in an array

"""
Given an unsorted integer array, print all pairs with a given difference k in it.
"""

from typing import List, Tuple 

class Solution:
    def findPair(self, nums : List[int], target: int) -> set[Tuple[int]]:
        
        hashset: set(Tuple[int]) = set(nums)
        # take an empty set 
        result: set = set()
    
        for num in hashset:
            # check if pair with the given difference exists
            if num - target in hashset:
                result.add((num - target, num))

        return result 


if __name__ == "__main__":
    solution = Solution()

    s1 = solution.findPair([1, 5, 2, 2, 2, 5, 5, 4], 3)

    print(s1)

