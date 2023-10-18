# Design HashMap


"""
Design a HashMap without using any built-in hash table libraries.

Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
"""

# Runtime: 235ms (Beats 55.73% of users with Python)
# Memory: 17.8MB (Beats 33.27% of users with Python)

from typing import List

class ListNode:
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap(object):
    def __init__(self) -> None:
        # The maximum length of the hashmap will be 1000 to store values
        self.map: List[ListNode] = [ListNode() for i in range(1000)]

    def put(self, key: int, value: int) -> None:
        # Only save within than lenght 
        cur = self.map[key % len(self.map)]
        while cur.next: 
            # If the next key of the current position matches the key you want to add,
            if cur.next.key == key:
                # Update the value
                cur.next.val = value
                return
            # Keep searching
            cur = cur.next
        # If they don't match, then add it 
        cur.next = ListNode(key, value)        
        

    def get(self, key: int) -> int:
        # Only search within than lenght 
        cur = self.map[key % len(self.map)].next
        
        while cur and cur.key != key:
            # Keep searching
            cur = cur.next

        if cur:
            # Return the value
            return cur.val
        return -1
        

    def remove(self, key: int) -> None:
        # Only save within than lenght 
        cur = self.map[key % len(self.map)]

        while cur.next and cur.next.key != key:
            # Keep searching
            cur = cur.next
        
        # If the next key of the current position matches the key you want to delete,
        if cur and cur.next:
            #then the pointer will point to the next one to delete it
            cur.next = cur.next.next

