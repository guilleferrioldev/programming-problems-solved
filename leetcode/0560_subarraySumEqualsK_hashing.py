# Subarray Sum Equals K

"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.
"""

# Runtime: 222ms (Beats 60.60% of users with Python)
# Memory: 15.7MB (Beats 93.26% of users with Python)

from typing import List

class Solution(object):
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Hashmap to save all the values
        hashmap = {0 : 1}
        # Variable to store count of number of subarrays
        count = 0
        # Variable to start the addition
        currSum = 0
        for num in nums:
            # Add each value of the array
            currSum += num
            # If the sum - k exists in the hashmap, then there is a subarray
            if currSum - k in hashmap:
                count += hashmap[currSum - k]
            # Save each sum in the hashmap
            hashmap[currSum] = hashmap.get(currSum, 0) + 1
        
        return count

if __name__ == "__main__":
    solution = Solution()

    s1 = solution.subarraySum([1,1,1], 2)
    s2 = solution.subarraySum([1,2,3], 3)

    print(s1, s2)








