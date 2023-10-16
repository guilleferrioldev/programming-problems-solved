# Group Anagrams

"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
 
"""

# Runtime: 68ms (Beats 73.87% of users with Python)
# Memory: 17.3MB (Beats 75.87% of users with Python)

from collections import defaultdict
from typing import List

class Solution(object):
    def groupAnagrams(self, strs: List[str]) -> List[str]:
        # Hashmap to save all lists
        hashmap: defaultdict[str, list] = defaultdict(list)
        
        # Add to the lists all the values that correspond to itself ordered
        for word in strs:
            hashmap["".join(sorted(word))].append(word)
        
        return list(hashmap.values())


if __name__ == "__main__":
    solution = Solution()

    s1 = solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    s2 = solution.groupAnagrams([""])
    s3 = solution.groupAnagrams(["a"])

    print(s1, s2, s3)
