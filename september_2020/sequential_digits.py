from typing import List


class Solution:
    """
    An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

    Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

    Example 1:

    Input: low = 100, high = 300
    Output: [123,234]

    Example 2:

    Input: low = 1000, high = 13000
    Output: [1234,2345,3456,4567,5678,6789,12345]

    Constraints: 10 <= low <= high <= 10^9

    Show Hint #1

        Generate all numbers with sequential digits and check if they are in the given range.

    Show Hint #2

        Fix the starting digit then do a recursion that tries to append all valid digits.
    """

    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        ans = []
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                st = int(s[i : j + 1])
                if st >= low and st <= high:
                    ans.append(st)
                elif st > high:
                    break
        ans.sort()
        return ans
