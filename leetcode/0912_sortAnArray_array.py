# 912 Sort an Array

"""
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible
"""

# Runtime: 1556ms (Beats 27.86% of users with Python)
# Memory: 23.2MB (Beats 25.76% of users with Python)

from typing import List

class Solution(object):
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(first_sublist: List[int], second_sublist: List[int]) -> List[int]:
            i = j = 0
            merged_list = []

            while i < len(first_sublist) and j < len(second_sublist):
                if first_sublist[i] < second_sublist[j]:
                    merged_list.append(first_sublist[i])
                    i += 1
                else:
                    merged_list.append(second_sublist[j])
                    j += 1
                    
            while i < len(first_sublist):
                merged_list.append(first_sublist[i])
                i += 1
    
            while j < len(second_sublist):
                merged_list.append(second_sublist[j])
                j += 1
    
            return merged_list
        
        def merge_sort(unsorted_list: List[int]) -> List[int]:
            if len(unsorted_list) == 1:
                return unsorted_list
            
            mid_point = len(unsorted_list)//2
            first_half = unsorted_list[:mid_point]
            second_half = unsorted_list[mid_point:]
    
            half_a = merge_sort(first_half)
            half_b = merge_sort(second_half)
    
            return merge(half_a, half_b)
        
        return merge_sort(nums)
    
if __name__ == "__main__":
    solution = Solution()
    
    s1 = solution.sortArray([5,2,3,1])
    s2 = solution.sortArray([5,1,1,2,0,0])
    
    print(s1, s2)