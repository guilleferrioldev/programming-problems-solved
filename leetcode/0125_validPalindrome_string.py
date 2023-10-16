# Valid Palindrome

"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

# Runtime: 22ms (Beats 90.42% of users with Python)
# Memory: 14.74MB (Beats 53.84% of users with Python)

class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        
        result = "".join(char for char in s.lower() if char.isalnum())
        
        return result == result[::-1]

if __name__ == "__main__":
    solution = Solution()   

    s1 = solution.isPalindrome("A man, a plan, a canal: Panama")
    s2 = solution.isPalindrome("race a car")
    s3 = solution.isPalindrome("  ")

    print(s1, s2, s3)




