class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def deleteAtTail(self, head):
        if not head or head.next is None:
            return None
        
        current = head

        while current.next.next is not None:
            current = current.next
        
        current.next = None
        return head
        

        
        

        
