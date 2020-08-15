class Solution:
    """
    Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
    This is case sensitive, for example "Aa" is not considered a palindrome here.

    Note:
    Assume the length of given string will not exceed 1,010.

    Example:

    Input:
    "abccccdd"

    Output:
    7

    Explanation:
    One longest palindrome that can be built is "dccaccd", whose length is 7.

    """

    def longestPalindrome(self, s: str) -> int:
        count = 0
        mapping = {}

        for c in s:
            mapping[c] = mapping.get(c, 0) + 1
            if mapping[c] == 2:
                count += 2
                mapping[c] = 0

        for m in mapping.values():
            if m == 1:
                count += 1
                break

        return count
