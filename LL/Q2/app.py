class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class Solution:
    def insertAtHead(self, head, val): # Here val is the value which we're gonna insert
        new_node = Node(val)
        new_node.next = head
        return new_node

