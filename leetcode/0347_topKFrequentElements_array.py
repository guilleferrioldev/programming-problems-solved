# Top K Frequent Elements

"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

"""

# Runtime: 71ms (Beats 75.54% of users with Python)
# Memory: 16.50MB (Beats 88.54% of users with Python)

from collections import Counter
from typing import List

class Solution(object):
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        return [i[0] for i in Counter(nums).most_common(k)]
    

if __name__ == "__main__":
    solution = Solution()

    s1 = solution.topKFrequent([1,1,1,2,2,3], 2)
    s2 = solution.topKFrequent([1], 1)

    print(s1 , s2)

