# Determine whether two strings are anagram or not

"""
Given two strings, determine whether they are anagrams.

Any word that exactly reproduces the letters in another order is an anagram. In other words
, X and Y are anagrams if by rearranging the letters of X, we can get Y using all the original 
letters of X exactly once.
"""


class Solution:
    def isAnagram(self, word1: str, word2: str) -> bool:
        
        return sorted(word1) == sorted(word2)


class Solution2:
    def isAnagram(self, X, Y):
 
        # if X's length is not the same as Y's, they can't be an anagram
        if len(X) != len(Y):
            return False
 
        # create an empty dictionary
        freq = {}
 
        # maintain the count of each character of `X` in the dictionary
        for i in range(len(X)):
            freq[X[i]] = freq.get(X[i], 0) + 1
 
        # do for each character `y` of `Y`
        for i in range(len(Y)):
 
            # if `y` is found not in the dictionary, i.e., either `y` is not present
            # in string `X` or has more occurrences in string `Y`
            if not Y[i] in freq:
                return False
    
            # decrease the frequency of `y` on the dictionary
            freq[Y[i]] = freq[Y[i]] - 1
 
            # if its frequency becomes 0, erase it from the dictionary
            if freq[Y[i]] == 0:
                del freq[Y[i]]
 
        # return true if the dictionary becomes empty
        return not freq

if __name__ == "__main__":
    solution = Solution()
    solution2 = Solution2()

    s1 = solution.isAnagram("silent" ,"listen")
    s2 = solution2.isAnagram("tommarvoloriddle" ,"iamlordvoldemort")

    print(s1, s2)

