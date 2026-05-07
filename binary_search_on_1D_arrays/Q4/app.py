# FIND MINIMUM IN ROTATED SORTED ARRAY

class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1
        currentMin = nums[left]

        while left <= right:
            mid = left + (right - left) // 2

            # Left half is sorted
            if nums[left] <= nums[mid]:
                currentMin = min(currentMin, nums[left])
                left = mid + 1

            # Right half is sorted
            else:
                currentMin = min(currentMin, nums[mid])
                right = mid - 1
        return currentMin

