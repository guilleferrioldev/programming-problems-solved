# Contains Duplicate 

"""
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
"""

# Runtime: 419ms (Beats 83.48% of users with Python)
# Memory: 29.1MB (Beats 47.69% of users with Python)

from typing import List

# Iterative solution
class Solution(object):
    def containsDuplicate(self, nums: List[int]) -> bool:
        # A hash to save all the values
        hashset: set[int] = set()
        
        # iterate through the array and return True if the number is already in the hash, otherwise return false
        for i in nums:
            # check if the value exists or not in the hashset, then return False or save it  
            if i not in hashset:
                hashset.add(i)
            else:
                return True 
        return False

if __name__ == "__main__":
    solution = Solution()

    s1 = solution.containsDuplicate([1,2,3,1])
    s2 = solution.containsDuplicate([1,2,3,4])
    s3 = solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2])
    
    print(s1, s2, s3)
