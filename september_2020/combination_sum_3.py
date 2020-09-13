from typing import List


class Solution:
    """
    Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

    Note:

        All numbers will be positive integers.
        The solution set must not contain duplicate combinations.

    Example 1:

    Input: k = 3, n = 7
    Output: [[1,2,4]]

    Example 2:

    Input: k = 3, n = 9
    Output: [[1,2,6], [1,3,5], [2,3,4]]
    """

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(k, start, x, n, l, ans):
            if start == k:
                if sum(l) == n:
                    ans.append(list(l))
                return
            elif start > k or len(l) > k:
                return
            else:
                for i in range(x, 10):
                    l.append(i)
                    backtrack(k, start + 1, x + 1, n, l, ans)
                    l.pop()
            return ans

        return backtrack(k, 0, 1, n, [], [])
