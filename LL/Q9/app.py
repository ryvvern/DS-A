class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def reverseList(self, head):
        prev = None
        current = head

        while current is not None:
            # save the next node
            next_node = current.next

            # point the current node to prev
            current.next = prev

            # move prev to the current node
            prev = current

            # move current to the next node
            current = next_node
        
        # return the new head
        return prev
