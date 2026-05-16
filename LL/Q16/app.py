class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class Solution:
    def findDuplicate(self, nums):
        # phase 1: find meeting point
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        # find entry point of cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
    

