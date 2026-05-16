class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class Solution:
    def addTwoNumbers(self, l1, l2):

        dummy = Node(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            digit = total % 10
            carry = total // 10

            # create new node and attach
            current.next = Node(digit)
            current = current.next

            # move both lists forward
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            