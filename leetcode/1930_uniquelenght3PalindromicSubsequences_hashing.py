# Unique Length-3 Palindromic Subsequences


"""
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters 
(can be none) deleted without changing the relative order of the remaining characters.

"""

# Runtime: 164ms (Beats 98.75% of users with Python)
# Memory: 14.6MB (Beats 72.50% of users with Python)

class Solution(object):
    def countPalindromicSubsequence(self, s: str) -> int:
    
        count: int = 0
        # Convert the string to set
        chars: set[str] = set(s)
        
        for char in chars:
            # Search for the caracter in both directions in the string
            first, last = s.find(char), s.rfind(char)
            # Count the number of different characters between both letters
            count += len(set(s[first+1:last]))
        
        return count

if __name__ == "__main__":
    solution = Solution()

    s1 = solution.countPalindromicSubsequence("aabca")
    s2 = solution.countPalindromicSubsequence("adc")
    s3 = solution.countPalindromicSubsequence("bbcbaba")
    
    print(s1, s2 , s3)
