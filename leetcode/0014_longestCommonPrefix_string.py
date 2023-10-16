# Longest Common Prefix 

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

# Runtime: 14ms (Beats 80.63% of users with Python)
# Memory: 13.5MB (Beats 67.64% of users with Python)

from typing import List

class Solution(object):
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Sort the list
        order: List[str] = sorted(strs)
        # Hash to store the values that are repeated
        hashstr: str = ""
        
        # Iterate through the length of the minimum between the last and first value
        for i in range(min(len(order[0]), len(order[-1]))):
            # The current positions must be the same 
            if order[0][i] != order[-1][i]:
                return hashstr
            # Save the values that are repeated
            hashstr += order[0][i]

        return hashstr  

if __name__ == "__main__":
    solution = Solution()

    s1 = solution.longestCommonPrefix(["flower","flow","flight"])
    s2 = solution.longestCommonPrefix(["dog","racecar","car"])

    print(s1, s2)
