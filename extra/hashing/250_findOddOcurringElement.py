# Find the odd occurring element in an array in a single traversal

"""
Given an integer array, duplicates are present in it in a way that all duplicates appear
an even number of times except one which appears an odd number of times. Find that odd
ºappearing element in linear time and without using any extra memory.
"""

# Function to find an odd occurring element in a given list
class Solution:
    def findOddOccuring(self, arr):
 
        xor = 0
        for i in arr:
            xor = xor ^ i
    
        return xor
 
 
if __name__ == '__main__':
    solution = Solution()
    
    s1 = solution.findOddOccuring([4, 3, 6, 2, 6, 4, 2, 3, 4, 3, 3])
    
    print(s1)
