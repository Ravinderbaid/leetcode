from typing import List


class Solution:
    """
    Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
    Find all the elements that appear twice in this array.
    """

    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] = -nums[abs(num) - 1]
            else:
                ans.append(abs(num))
        return ans
