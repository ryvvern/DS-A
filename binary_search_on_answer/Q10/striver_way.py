# KOKO EATING BANANAS
import math

class Solution:
    def calc_hr_rate(self, arr, hourly):
        total_hrs = 0
        for i in range(len(arr)):
            total_hrs += math.ceil(arr[i] / hourly)
        return total_hrs

    def minEatingSpeed(self, arr, h):
        left = 1
        right = max(arr)
        ans = right  # ← initialize to max possible speed

        while left <= right:
            mid = left + (right - left) // 2
            total_hrs = self.calc_hr_rate(arr, mid)
            if total_hrs <= h:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans