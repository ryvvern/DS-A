# Find How Many Times a Sorted Array Was Rotated

class Solution:
    def countRotations(self, nums):
        left = 0
        right = len(nums) - 1
        currMin = 0

        while left <= right:
            mid = left + (right - left) // 2

            # Left half is sorted
            if nums[left] <= nums[mid]:
                if nums[left] < nums[currMin]:
                    currMin = left
                left = mid + 1
            
            # Right half is sorted
            else:
                if nums[mid] < nums[currMin]:
                    currMin = mid
                right = mid - 1

        return currMin