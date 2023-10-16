# Replace Elements with Greatest Element on Right Side

"""
Given an array arr, replace every element in that array with the greatest element
among the elements to its right, and replace the last element with -1.

After doing so, return the array.
"""

# Runtime: 543ms (Beats 51.38% of users with Python)
# Memory: 14.61MB (Beats 78.45% of users with Python)

from typing import List

class Solution(object):
    def replaceElements(self, arr: List[int]) -> List[int]:
        # -1 will be the first maximum value from right to left
        rightMax: int = -1
        
        # reverse iteration
        for i in range(len(arr) -1, -1, -1):
            # newMax = max(oldmax, current position)
            newMax: int = max(rightMax, arr[i])
            # current position take the value of the max
            arr[i]: int = rightMax
            # Update the rightMax with the newMax
            rightMax: int = newMax
        
        return arr


if __name__ == "__main__":
    solution = Solution()

    s1 = solution.replaceElements([17,18,5,4,6,1])
    s2 = solution.replaceElements([400])

    print(s1, s2)
