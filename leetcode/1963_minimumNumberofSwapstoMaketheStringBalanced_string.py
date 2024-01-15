# Minimum Number of Swaps to Make the String Balanced

"""
You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

A string is called balanced if and only if:

    It is the empty string, or
    It can be written as AB, where both A and B are balanced strings, or
    It can be written as [C], where C is a balanced string.

You may swap the brackets at any two indices any number of times.

Return the minimum number of swaps to make s balanced.
"""

# Runtime: 269ms (Beats 81.01% of users with Python)
# Memory: 31.37MB (Beats 81.01% of users with Python)

class Solution1(object):
    def minSwaps(self, s: str) -> int:
        extraClose, maxClose = 0, 0 

        for char in s: 
            if char == "[":
                extraClose -= 1
            else:
                extraClose += 1

            maxClose = max(maxClose, extraClose)

        return (maxClose + 1)// 2
    
class Solution2(object):
    def minSwaps(self, s: str) -> int:
        count = 0 
        
        for char in s:
            if char == "[":
                count += 1 
            elif count > 0:
                count -= 1
        return (count + 1) // 2
    
if __name__ == "__main__":
    solution1 = Solution1()
    solution2 = Solution2()
    
    s1 = solution1.minSwaps("][][")
    s2 = solution2.minSwaps("]]][[[")
    s3 = solution1.minSwaps("[]")
    
    print(s1, s2, s3)