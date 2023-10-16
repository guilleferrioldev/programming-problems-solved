# Word Pattern

"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between
a letter in pattern and a non-empty word in s.
"""

# Runtime: 16ms (Beats 40.20% of users with Python)
# Memory: 13.20MB (Beats 93.86% of users with Python)

class Solution(object):
    def wordPattern(self, pattern: str, s: str) -> bool:

        if len(pattern) != len(s.split(" ")):
            return False
        
        return len(set(pattern)) == len(set(s.split(" "))) == len(set(zip(pattern, s.split(" "))))

if __name__ == "__main__":
    solution = Solution()

    s1 = solution.wordPattern("abba","dog cat cat dog")
    s2 = solution.wordPattern("abba","dog cat cat fish")
    s3 = solution.wordPattern("aaaa","dog cat cat dog")

    print(s1, s2, s3)
