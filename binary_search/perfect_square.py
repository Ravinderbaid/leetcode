class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 1:
            return True
        high = num // 2
        low = 0

        while low <= high:
            mid = (high + low) // 2
            mid_sq = mid * mid
            if mid_sq == num:
                return True
            elif mid_sq < num:
                low = mid + 1
            else:
                high = mid - 1
        return False
