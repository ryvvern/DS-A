# Insert at Tail

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class Solution:
    def insertAtTail(self, head, val):
        new_node = Node(val)

        if head == None:
            return new_node
        
        current = head
        while current.next is not None:
            current = current.next
        current.next = new_node
        return head
