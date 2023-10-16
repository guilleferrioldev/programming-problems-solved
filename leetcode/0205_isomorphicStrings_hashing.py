# Isomorphic Strings

"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. 
No two characters may map to the same character, but a character may map to itself.
"""

# Runtime: 20ms (Beats 82.94% of users with Python)
# Memory: 16.2MB (Beats 12.77% of users with Python)

class Solution(object):
    def isIsomorphic(self, s: str, t: str) -> bool:

       return len(set(s)) == len(set(t)) == len(set(zip(s,t)))


if __name__ == "__main__":
   solution = Solution()

   s1 = solution.isIsomorphic("egg", "add")
   s2 = solution.isIsomorphic("foo", "bar")
   s3 = solution.isIsomorphic("paper", "title")
   
   print(s1, s2, s3)
    
