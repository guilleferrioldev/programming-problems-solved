# Encode and Decode Strings

"""
Design an algorithm to encode a list of strings to a string.
The encoded string is then sent over the network and is decoded back to the original list of strings.

"""

from typing import List

class Solution:
    def encode(self, strs: List[str]) -> List[str]:
        return ':;'.join(strs)
    
    def decode(self, string: str) -> List[str]:
        # write your code here
        return string.split(":;")

if __name__ == "__main__":
    solution = Solution()

    s1_encode = solution.encode(["lit","code","love","you"])
    s1_decode = solution.decode(s1_encode)
    
    s2_encode = solution.encode(["we", "say", ":", "yes"])
    s2_decode = solution.decode(s2_encode)

    print(s1_decode, s2_decode)   
