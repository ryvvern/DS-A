# FIRST & LAST OCCURENCE OF THE ELEMENT

class Solution:
    def searchFirst(self, nums, target):

        left = 0
        right = len(nums) - 1
        first = -1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                first = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return first
    
    def searchLast(self, nums, target):

        left = 0
        right = len(nums) - 1
        last = -1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                last = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return last
    
    def searchRange(self, nums, target):
        first = self.searchFirst(nums, target)
        last = self.searchLast(nums, target)
        return [first,last]






        