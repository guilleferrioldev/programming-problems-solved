# Palindrome Number

"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""

# Runtime: 33ms (Beats 81.96% of users with Python)
# Memory: 13.1MB (Beats 90.61% of users with Python)

class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        # Special cases: if x is negative or if its last digit is 0
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        # Reverse half of the number
        reversed_num : int = 0
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        
        # When the length is an odd number, we can get rid of the middle digit by reversed_num/10
        # For example, when the input is 12321, at the end of the while loop we get x = 12, reversed_num = 123, since 
        # the middle digit doesn't matter in palindromic (it will always equal to itself), we can simply get rid of it.
        return x == reversed_num or x == reversed_num // 10


class Solution2(object):
    def isPalindrome(self, x: int) -> bool:

        return str(x) == str(x)[::-1]


if __name__ == "__main__":
    solution = Solution()
    solution2 = Solution2()

    s1 = solution.isPalindrome(121)
    s2 = solution2.isPalindrome(-121)
    s3 = solution.isPalindrome(10)

    print(s1, s2, s3)
