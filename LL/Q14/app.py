class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None

class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        
        # pass 1: create all copy nodes in a hash map
        node_map = {}
        current = head
        while current:
            node_map[current] = Node(current.val)
            current = current.next
        
        # pass 2: assign the next and random pointers
        current = head
        while current:
            if current.next:
                node_map[current].next = node_map[current.next]
            if current.random:
                node_map[current].random = node_map[current.random]
            current = current.next
        return node_map[head]


