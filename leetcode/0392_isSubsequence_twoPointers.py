# Is Subsequence

"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a
subsequence of "abcde" while "aec" is not).
"""

# Runtime: 11ms (Beats 85.58% of users with Python)
# Memory: 13.3MB (Beats 90.67% of users with Python)

class Solution(object):
    def isSubsequence(self, s: str, t: str) -> bool:
        # s must be subsequence of t
        if len(s) > len(t):
            return False
         
        i , j = 0, 0
         
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1 
            j += 1  

        return i == len(s)

if __name__ == "__main__":
    solution = Solution()

    s1 = solution.isSubsequence("abc", "ahbgdc")
    s2 = solution.isSubsequence("acb", "ahbgdc")
    s3 = solution.isSubsequence("axc", "ahbgdc")

    print(s1, s2, s3)
