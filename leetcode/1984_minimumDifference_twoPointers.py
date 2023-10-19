# Minimum Difference Between Highest and Lowest of K Scores

"""
You are given a 0-indexed integer array nums, where nums[i] represents the score of
the ith student. You are also given an integer k.

Pick the scores of any k students from the array so that the difference between the
highest and the lowest of the k scores is minimized.

Return the minimum possible difference.
"""

# Runtime: 73ms (Beats 47.66% of users with Python)
# Memory: 13.6MB (Beats 14.6% of users with Python)

from typing import List

class Solution(object):
    def minimumDifference(self, nums: List[int], k: int) -> int:
        differences = []
        nums = sorted(nums)
        
        #iterate to k positions before length
        for i in range(len(nums) - k + 1):
            diff = nums[i + k - 1] - nums[i]
            differences.append(diff)

        return min(differences)


class Solution2(object):
    def minimumDifference(self, nums: List[int], k: int) -> int:
        # Sort the array
        nums.sort()
        left , right = 0, k - 1
        result = float("inf")
        
        while right < len(nums):
            result = min(result, nums[right] - nums[left])
            left, right = left + 1, right + 1

        return result
            
if __name__ == "__main__":
    solution1 = Solution()
    solution2 = Solution2()

    s1 = solution1.minimumDifference([90], 1)
    s2 = solution2.minimumDifference([9, 4, 1, 7], 2)

    print(s1, s2)



