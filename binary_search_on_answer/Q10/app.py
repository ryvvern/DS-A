# KOKO EATING BANANAS
import math

class Solution:
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)

        while left < right:
            mid = left + (right - left) // 2
            total_hrs = sum(math.ceil(pile / mid) for pile in piles)

            if total_hrs <= h:
                right = mid
            else:
                left = mid + 1

        return left