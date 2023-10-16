# Can Place Flowers

"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, 
flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty
, and an integer n, return true if n new flowers can be planted in the flowerbed without violating
the no-adjacent-flowers rule and false otherwise.
"""

# Runtime: 109ms (Beats 94.55% of users with Python)
# Memory: 13.9MB (Beats 41.36% of users with Python)

from typing import List

class Solution(object):
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Increase list for better iteration
        flowerbed: List[int] = [0] + flowerbed + [0]
        
        # Check if the three adjacent positions are 0, then add a 1 in that position and subtract 1 from n
        for i in range(1, len(flowerbed)-1):
            if not flowerbed[i-1] and not flowerbed[i] and not flowerbed[i+1]:
                flowerbed[i]: int = 1
                n -= 1 

        return n <= 0 

if __name__ == "__main__":
    solution = Solution()

    s1 = solution.canPlaceFlowers([1,0,0,0,1], 1)
    s2 = solution.canPlaceFlowers([1,0,0,0,1,0,0], 2)
    s3 = solution.canPlaceFlowers([0,0,1,0,1], 1)
    
    print(s1, s2, s3)
