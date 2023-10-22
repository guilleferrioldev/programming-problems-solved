#  Merge Sorted Array

"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should 
be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

# Runtime: 12ms (Beats 94.5% of users with Python)
# Memory: 13MB (Beats 94.33% of users with Python)

# All three solutions follow the same strategy, adding the list nums2 to the end of the nums1

from typing import List

class Solution(object):
    def merge(self, nums1: List[int], m: int, nums2: List[int], n:int) -> None:

        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
        
        if n > 0:
            nums1[:n] = nums2[:n]


class Solution2(object):
    def merge(self, nums1: List[int], m: int, nums2: List[int], n:int) -> None:
        
        nums1[m:] = nums2[:n]
        nums1.sort()
        
class Solution3(object):
    def merge(self, nums1: List[int], m: int, nums2: List[int], n:int) -> None:
        
        for j in range(n):
            nums1[m+j] = nums2[j]
        nums1.sort()
            
if __name__ == "__main__":
    solution = Solution()
    solution2 = Solution2()
    solution3 = Solution3()

    s1 = solution.merge([1,2,3,0,0,0], 3, [2,5,6], 3)
    s2 = solution2.merge([1], 1, [], 0)
    s3 = solution3.merge([0], 0, [1], 1)




