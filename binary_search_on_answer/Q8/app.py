# SQUARE ROOT OF A NUMBER

class Solution:
    def mySqrt(nums, x):
        if x == 0 or x == 1:
            return x
        
        left = 1
        right = x // 2

        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        return answer