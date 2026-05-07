class Solution:
    def canMakeBouquets(self, bloomDay, day, m, k):
        bouquets = 0
        adjacent = 0

        for bloom in bloomDay:
            if bloom <= day:
                # flower has bloomed, count it
                adjacent += 1
                if adjacent == k:
                    # completed one bouquet
                    bouquets += 1
                    adjacent = 0
            else:
                adjacent = 0

        return bouquets >= m

    def minDays(self, bloomDay, m, k):
        # impossible case
        if m * k > len(bloomDay):
            return -1
        
        left = 1
        right = max(bloomDay)

        while left < right:
            mid = left + (right - left) // 2

            if self.canMakeBouquets(bloomDay, mid, m, k):
                right = mid
            else:
                left = mid + 1

        return left
            