# Delet at posiition

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class Solution:
    def deleteAtPosition(self, head, position):
        # empty list
        if not head:
            return None
        
        # delete at head
        if position == 0:
            head = head.next
            return head
        
        # traverse to node just before the target position
        current = head
        count = 0

        while current.next is not None and count < position - 1:
            current = current.next
            count += 1

        # out of bounds, position exceeds list length
        if current.next is None:
            return head
        
        # skip over the target node
        current.next = current.next.next
        
        return head