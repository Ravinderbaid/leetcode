from typing import List


class Solution:
    """
    Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 ≤ i ≤ j < n.

    Follow up: Could you do this in O(n) runtime?

    Example 1:
    Input: nums = [3,10,5,25,2,8]
    Output: 28
    Explanation: The maximum result is 5 XOR 25 = 28.

    Example 2:
    Input: nums = [0]
    Output: 0

    Example 3:
    Input: nums = [2,4]
    Output: 6

    Example 4:
    Input: nums = [8,10,2]
    Output: 10

    Example 5:
    Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
    Output: 127

    Constraints:
        1 <= nums.length <= 2 * 104
        0 <= nums[i] <= 231 - 1
    """

    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = {}

        def update_trie(x):
            # update trie with binary representation of x
            cur = trie
            for bit in format(x, "032b"):
                if bit not in cur:
                    cur[bit] = {}
                cur = cur[bit]
            cur["value"] = x
            return

        def best_match(x):
            # try to match with complement of x as much as possible
            # recall that for xor opertator
            # 1 xor 0 = 1
            # 0 xor 1 = 1
            # 0 xor 0 = 1 xor 1 = 0
            cur = trie
            for bit in format(x, "032b"):
                rev = "0" if bit == "1" else "1"
                if rev in cur:
                    cur = cur[rev]
                else:
                    cur = cur[bit]
            return cur["value"]

        for x in nums:
            update_trie(x)
        max_xor = 0
        for x in nums:
            # update global maximal xor result
            max_xor = max(max_xor, x ^ best_match(x))
        return max_xor
