# Find the Index of the First Occurrence in a String

"""
Given two strings needle and haystack, return the index of the first occurrence of needle 
in haystack, or -1 if needle is not part of haystack.
"""

class Solution(object):
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: # needle == "" 
            return 0
        
        # Longest-Prefix-Suffix
        lps = [0] * len(needle)

        prevLPS, i = 0, 1
        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            elif prevLPS == 0:
                lps[i] = 0
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]

        i = 0  # ptr for haystack
        j = 0  # ptr for needle
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
            if j == len(needle):
                return i - len(needle)
        return -1
    
if __name__ == "__main__":
    solution = Solution()
    
    s1 = solution.strStr("sadbutsad", "sad")
    s2 = solution.strStr("leetcode", "leeto")
    s3 = solution.strStr("hello", "ll")
    
    print(s1, s2, s3)
        