import math

class Solution:
    def smallestDivisor(self, nums, threshold):
        minDivisor = 1
        maxDivisor = max(nums)

        while minDivisor < maxDivisor:
            mid = minDivisor + (maxDivisor - minDivisor) // 2
            total = sum(math.ceil(num / mid) for num in nums)

            if total <= threshold:
                maxDivisor = mid
            else:
                minDivisor = mid + 1
                
        return minDivisor
            
        