# Reverse String

"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""

# Runtime: 121ms (Beats 94.35% of users with Python)
# Memory: 20.8MB (Beats 80.8% of users with Python)

from typing import List

class Solution(object):
    def reverseString(self, s: List[str]) -> None:
    
        start , end = 0, len(s) - 1
        
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

if __name__ == "__main__":
    solution = Solution()

    s1 = solution.reverseString(["h","e","l","l","o"])
    s2 = solution.reverseString(["H","a","n","n","a","h"])
    
    
