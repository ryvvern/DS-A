# NTH ROOT OF A NUMBER

class Solution:
    def nthRoot(self, n, x):
        if x == 0 or x == 1:
            return x
        
        left = 1
        right = x

        while left <= right:
            mid = left + (right - left) // 2
            mid_nth = mid ** n

            if mid_nth == x:
                return mid
            elif mid_nth < x:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans