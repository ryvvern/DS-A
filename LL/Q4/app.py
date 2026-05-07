class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def insertAtPosition(self, head, val, position):
        new_node = Node(val)

        if position == 0:
            new_node.next = head
            return new_node
        
        current = head
        count = 0

        while current.next is not None and count < position - 1:
            current = current.next
            count += 1
        
        new_node.next = current.next
        current.next = new_node
    
        return head

        