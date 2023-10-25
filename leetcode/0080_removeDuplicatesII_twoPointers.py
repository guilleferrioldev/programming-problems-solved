# Remove Duplicates from Sorted Array II

"""
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element
appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in
the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k
elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
"""

# Runtime: 30ms (Beats 77.21% of users with Python)
# Memory: 12.99MB (Beats 99.45% of users with Python)


from typing import List

class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        pos: int = 0
        
        for num in nums: 
            if pos < 2 or num > nums[pos-2]:
                nums[pos] = num
                pos += 1

        return pos


if __name__ == "__main__":
    solution = Solution()

    s1 = solution.removeDuplicates([1,1,1,2,2,3])
    s2 = solution.removeDuplicates([0,0,1,1,1,1,2,3,3])
    s3 = solution.removeDuplicates([0,0])
    
    print(s1, s2, s3)
