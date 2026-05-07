# SINGLE ELEMENT IN A SORTED ARRAY

class Solution:
    def singleNonDuplicate(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # Make mid even for consistent pair checking
            if mid % 2 == 1:
                mid -= 1

            # Pair is intact — single is to the right
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            # Pair is broken — single is here or to the left
            else:
                right = mid

        return nums[left]