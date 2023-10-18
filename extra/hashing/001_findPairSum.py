# Find a pair with the given sum in an array

"""
Given an unsorted integer array, find a pair with the given sum in it.
"""

from typing import List, Tuple

class Solution:
    def findPair(self, nums: List[int], target: int) -> set[Tuple[int]]:
        # create an empty set
        result: List[List[int]] = set()
        # create an empty dictionary
        hashtable: dict[int, int] = dict()

        for index, value in enumerate(nums):
            diff = target - value
            # check if difference exists
            if diff in hashtable:
                # if the difference is seen before, then save the tuple in result
                result.add((nums[hashtable.get(diff)], nums[index]))
            # store index of the current element in the dictionary  
            hashtable[value] = index 

        return result


if __name__ == "__main__":
    solution = Solution()
    
    s1 = solution.findPair([8, 7, 2, 5, 3, 1], 10)
    s2 = solution.findPair([5, 2, 6, 8, 1, 9], 12)

    print(s1, s2)


