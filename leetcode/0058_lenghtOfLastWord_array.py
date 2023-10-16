# Length of Last Word

"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
consisting of non-space characters only.
"""

# Runtime: 10ms (Beats 84.91% of users with Python)
# Memory: 13.40MB (Beats 84.65% of users with Python)

class Solution(object):
    def lengthOfLastWord(self, s: str) -> int:
        # strip to delete the spaces at the begining and end of the string, and split the string into a list without spaces
        return len(s.strip().split(" ")[-1])

if __name__ == "__main__":
    solution = Solution()

    s1 = solution.lengthOfLastWord("Hello World")
    s2 = solution.lengthOfLastWord("   fly me   to   the moon  ")
    s3 = solution.lengthOfLastWord("luffy is still joyboy")
    
    print(s1, s2, s3)

