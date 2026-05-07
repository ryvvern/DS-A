class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def deleteAtHead(self, head):
        if not head:
            return None
        
        head = head.next
        return head