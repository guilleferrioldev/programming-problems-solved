"""Given an array of integers that are out of order, determine the bounds of the smallest
window that must be sorted in order for the entire array to be sorted"""

from typing import List, Tuple

class Solution: # O(nlogn)
    def smallestWindow(self, nums: List[int]) -> Tuple[int, int]:
        left , rigth = None, None 
        sorted_nums = sorted(nums)

        for index in range(len(nums)):
            if nums[index] != sorted_nums[index] and left is None:
                left = index
            elif nums[index] != sorted_nums[index]:
                rigth = index 

        return left, rigth

class Solution2: # O(n)
    def smallestWindow(self, array: List[int]) -> Tuple[int, int]:
        left, right = None, None
        max_seen, min_seen = -float("inf"), float("inf")

        for i in range(len(array)):
            max_seen = max(max_seen, array[i])
            if array[i] < max_seen:
                right= i

        for i in range(len(array) - 1, -1, -1):
            min_seen = min(min_seen, array[i])
            if array[i] > min_seen:
                left= i
        
        return left, right

if __name__ == "__main__":
    solution = Solution()
    solution2 = Solution2()

    s1 = solution.smallestWindow([3, 7, 5, 6, 9])
    s2 = solution2.smallestWindow([3, 7, 5, 6, 9])

    print(s1, s2)


