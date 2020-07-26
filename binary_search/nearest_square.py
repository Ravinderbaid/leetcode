class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        low = 0
        high = x // 2
        while low <= high:
            mid = (low + high) // 2
            mid_sq = mid * mid
            if mid_sq == x:
                return mid
            elif mid_sq > x:
                high = mid - 1
            else:
                low = mid + 1

        return high
