# Valid Anagram

"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.
"""

# Runtime: 24ms (Beats 91.59% of users with Python)
# Memory: 13.6MB (Beats 94.76% of users with Python)

class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if both lenghts are equals, then return False 
        if len(s) != len(t):
            return False
        
        # Hashmaps to keep count of the values of both strings 
        hashmap_s: dict[str, int] = {}
        hashmap_t: dict[str, int] = {}
        
        # Iterate through both strings and save the number of times each value appears
        for char in s:
            hashmap_s[char]: int = hashmap_s.get(char, 0) + 1
        
        for char in t:
            hashmap_t[char]: int = hashmap_t.get(char, 0) + 1
        
        # Compare between to hashmaps
        return hashmap_s == hashmap_t

if __name__ == "__main__":
    solution = Solution()


    s1 = solution.isAnagram("anagram", "nagaram")
    s2 = solution.isAnagram("rat", "car")

    print(s1, s2)
