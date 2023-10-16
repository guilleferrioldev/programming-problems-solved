# Valid Palindrome II 

"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
"""

# Runtime: 50ms (Beats 95.37% of users with Python)
# Memory: 14.5MB (Beats 17.82% of users with Python)

class Solution(object):
    def validPalindrome(self, s: str) -> bool:

        if len(s) <= 2:
            return True
        
        if s == s[::-1]:
            return True

        # Point to the beginning and the end of the string
        start, end = 0, len(s) - 1
        
        # Iterate as long as the start and end value are equal
        while start < end:
            # When the values are different
            if s[start] != s[end]:
                # Delete this value and return the bool
                first = s[0: start] + s[start+1:]
                second = s[0: end] + s[end+1:]
                return first == first[::-1] or second == second[::-1]
            # Increment and decrement the values looking for the middle of the string
            start += 1
            end -= 1


if __name__ == "__main__":
   solution = Solution()

   s1 = solution.validPalindrome("aba")
   s2 = solution.validPalindrome("abca")
   s3 = solution.validPalindrome("abc")

   print(s1, s2, s3)
