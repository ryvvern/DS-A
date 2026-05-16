class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        slow = head
        fast = head

        for _ in range(n):
            fast = fast.next
        
        if fast is None:
            return head.next
        
        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        
        return head
    
