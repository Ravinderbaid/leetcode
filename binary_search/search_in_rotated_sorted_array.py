from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        if high < 0:
            return -1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if nums[low] > target and nums[low] <= nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[high] < target and nums[high] > nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1


s = Solution()
s.search([4, 5, 6, 7, 0, 1, 2], 0)
