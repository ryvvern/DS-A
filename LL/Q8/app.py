class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class Solution:
    def length(self, head):
        if not head:
            return 0

        current = head
        count = 0

        while current is not None:
            count += 1
            current = current.next
        return count
