# Determine if two integers are equal without using comparison and arithmetic operators

"""
This post will discuss how to determine whether two integers are equal without using comparison operators (==, !=, <, >, <=, >=) and arithmetic operators (+, -, *, /, %).
"""

class Solution:
    def checkForEquality(self, x: int, y: int) -> bool:
        # Create an empty map
        dicc: set[int] = set()
        # Add the value of x
        dicc.add(x)
        # Returns True if the value of y matches the value of x that is in the set
        return y in dicc
 
if __name__ == '__main__':
    solution = Solution()

    s1 = solution.checkForEquality(1, 2)
    s2 = solution.checkForEquality(2, 2)
    
    print(s1, s2)

    


