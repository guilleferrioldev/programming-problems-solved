# Find duplicates within a range k in an array

"""
Given an array and a positive number k, check whether the array contains any duplicate elements 
within the range k. If k is more than the array’s size, the solution should check for duplicates
in the complete array.
"""

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int], target: int) -> bool:
        # Hashmap to store all the values with its index
        hashmap: dict[int, int] = dict()

        for index, value in enumerate(nums):
            # If the value exists in the hashmap and the difference between the index 
            # and the index of the value that exists hashmap is less than the target, returns True
            if value in hashmap and (index - hashmap.get(value) <= target):
                return True 
            # Save the value and its index in the hashmap
            hashmap[value] = index
        
        return False

if __name__ == "__main__":
    solution = Solution()


    s1 = solution.findDuplicate([5, 6, 8, 2, 4, 8, 6, 9], 4)
    s2 = solution.findDuplicate([5, 6, 8, 2, 4, 8, 6, 9], 2)

    print(s1, s2)


