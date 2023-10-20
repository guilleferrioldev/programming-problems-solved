# 1768. Merge Strings Alternately

"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order,
starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""

# Runtime: 10ms (Beats 88.86% of users with Python)
# Memory: 13.49MB (Beats 10.29% of users with Python)

class Solution(object):
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result: str = ""
        i: int = 0
        
        while i < min(len(word1), len(word2)):
            result: str = result + word1[i] + word2[i]
            i += 1 

        return result + word1[i:] + word2[i:] 


if __name__ == "__main__":
    solution = Solution()

    s1 = solution.mergeAlternately("abc", "pqr")
    s2 = solution.mergeAlternately("ab", "pqrs")
    s3 = solution.mergeAlternately("abcd", "pq")

    print(s1, s2, s3)
