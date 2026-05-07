import math

class Solution:
    def canShip(self, weights, capacity, d):
        currentWeight = 0
        numberOfDays = 1

        for weight in weights:
            if currentWeight + weight > capacity:
                numberOfDays += 1
                currentWeight = 0
            currentWeight += weight

        return numberOfDays <= d

    def shipWithinDays(self, weights, d):
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = left + (right - left) // 2

            if self.canShip(weights, mid, d):
                right = mid
            else:
                left = mid + 1

        return left