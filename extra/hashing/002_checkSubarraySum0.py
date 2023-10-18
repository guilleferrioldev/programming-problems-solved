# Check if a subarray with 0 sum exists or not 

"""
Given an integer array, check if it contains a subarray having zero-sum.
"""


class Solution:
    def hasZeroSumSublist(self, nums):
        # create an empty set to store the sum of elements of each
        # sublist `nums[0…i]`, where `0 <= i < len(nums)`
        # insert 0 into the set to handle the case when sublist with
        # zero-sum starts from index 0
        hashset = {0}
        
        count = 0
        for num in nums:
            # sum of elements so far
            count += num
            # if the sum is seen before, we have found a sublist with zero-sum
            if count in hashset:
                return True 
            # insert sum so far into the set
            hashset.add(count)

        return False            

if __name__ == "__main__":
    solution = Solution()

    s1 = solution.hasZeroSumSublist([3, 4, 3, 1, 3, 1, -4, -2, -2])

    print(s1)

