# Valid Parentheses

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.
"""

# Runtime: 10ms (Beats 90.43% of users with Python)
# Memory: 13.1MB (Beats 99.30% of users with Python)

class Solution(object):
    def isValid(self, s: str) -> bool:
        Map = {")": "(",
               "}": "{",
               "]": "["}
        stack = []

        for char in s:
            if char not in Map:
                stack.append(char)
                continue 
            if not stack or stack[-1] != Map[char]:
                return False
            stack.pop()

        return not stack


if __name__ == "__main__":
    solutiom = Solution()

    s1 = solutiom.isValid("()")
    s2 = solutiom.isValid("()[]{}")
    s3 = solutiom.isValid("(]")

    print(s1, s2, s3)
