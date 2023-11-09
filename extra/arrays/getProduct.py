"""Given an array of integers, return a new array such that each element at index i of
the new array is the product of all the numbers in the original array except the one
at i."""

from operator import mul
from functools import reduce
from typing import List

class Solution:
    def getProduct(self, nums: List[int]) -> List[int]:
        total = reduce(mul, nums)
        result = []

        for number in nums:
            result.append(total//number)

        return result 

if __name__ == "__main__":
    solution = Solution()

    s1 = solution.getProduct([1,2,3,4,5])
    s2 = solution.getProduct([3,2,1])

    print(s1, s2)

