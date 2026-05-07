# FIND PEAK ELEMENT

class Solution:
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # Mid is on the downward slope - peak is on the left
            if nums[mid] > nums[mid + 1]:
                right = mid
            
            # Mid is on an upward slope - peak is on the right
            else:
                left = mid + 1
        return left
