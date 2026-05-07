class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class Solution:
    def search(self, head, target):
        current = head

        while current:
            if current.val == target:
                return True
            current = current.next

        return False
        
    