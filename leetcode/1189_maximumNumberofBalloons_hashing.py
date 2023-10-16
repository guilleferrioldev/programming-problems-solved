# Maximum Number of Balloons

"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.
"""

# Runtime: 10ms (Beats 97.93% of users with Python)
# Memory: 13.36MB (Beats 87.91% of users with Python)

class Solution(object):
    def maxNumberOfBalloons(self, text: str) -> int:
        
        return min(text.count('b'),text.count('a'),text.count('l')//2,text.count('o')//2,text.count('n'))

if __name__ == "__main__":
    solution = Solution()   

    s1 = solution.maxNumberOfBalloons("balllllllllloooonnnnnnn")
    s2 = solution.maxNumberOfBalloons("loonbalxballpoon")
    s3 = solution.maxNumberOfBalloons("leetcode")

    print(s1, s2, s3)
