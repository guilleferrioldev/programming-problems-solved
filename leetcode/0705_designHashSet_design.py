# Design HashSet

"""
Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
"""

# Runtime: 253ms (Beats 35.63% of users with Python)
# Memory: 26.5MB (Beats 16.6% of users with Python)

class ListNode:
    """Class to create nodes in the linked list inside the hashset"""
    def __init__(self, key):
        self.key = key
        self.next = None


class MyHashSet(object):
    """Implementing the hashset"""
    def __init__(self) -> None:
        # The maximum length of the hashset will be 10**4 to store values
        self.set = [ListNode(0) for i in  range(10**4)]


    def add(self, key: int) -> None:
        # Only save within that length
        cur = self.set[key % len(self.set)]

        while cur.next:
            # If the next value of the current position matches the value you want to add, then it won't add it
            if cur.next.key == key:
                return
            # Keep searching
            cur = cur.next
        # If they don't match then add it
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        # Only save within that length
        cur = self.set[key % len(self.set)]

        while cur.next:
            # If the next value of the current position matches the value you want to delete,
            if cur.next.key == key:
                #then the pointer will point to the next one to delete it
                cur.next = cur.next.next
                return
            # Keep searching
            cur = cur.next
        

    def contains(self, key: int) -> bool:
        # Only search within that length
        cur = self.set[key % len(self.set)]

        while cur.next: 
            # If the next value of the current position matches the value being searched, then it returns True
            if cur.next.key == key:
                return True
            # Keep searching
            cur = cur.next
        # If they don't match then return False
        return False















