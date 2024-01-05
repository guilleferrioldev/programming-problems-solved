# Implement Trie (Prefix Tree)

"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. 
There are various applications of this data structure, such as autocomplete and spellchecker.
"""

# Runtime: 142ms (Beats 64.72% of users with Python)
# Memory: 40.76MB (Beats 35.63% of users with Python)

class Node:
    def __init__(self) -> None:
        self.children = {}
        self.is_leaf = False

class Trie(object):
    def __init__(self) -> None:
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            
            node = node.children[char]
            
        node.is_leaf = True
        

    def search(self, word: str) -> bool:
        node = self.root 
        
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
            
        return node.is_leaf

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
            
        return True