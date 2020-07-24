from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        set_bit = xor & ~(xor - 1)
        first = 0
        second = 0
        for num in nums:
            if set_bit & num:
                first ^= num
            else:
                second ^= num
        return [first, second]


s = Solution()
s.singleNumber([1, 2, 1, 2, 3, 5])
