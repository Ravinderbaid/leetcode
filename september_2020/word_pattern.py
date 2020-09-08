class Solution:
    """
    Given a pattern and a string str, find if str follows the same pattern.

    Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

    Example 1:

    Input: pattern = "abba", str = "dog cat cat dog"
    Output: true

    Example 2:

    Input:pattern = "abba", str = "dog cat cat fish"
    Output: false

    Example 3:

    Input: pattern = "aaaa", str = "dog cat cat dog"
    Output: false

    Example 4:

    Input: pattern = "abba", str = "dog dog dog dog"
    Output: false

    Notes:
    You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.

    """

    def wordPattern(self, pattern: str, str: str) -> bool:
        list_str = str.split(" ")
        if len(pattern) != len(list_str):
            return False
        s = set()
        d = {}
        for i in range(len(pattern)):
            if d.get(pattern[i]):
                if d[pattern[i]] != list_str[i]:
                    return False
            else:
                if list_str[i] not in s:
                    d[pattern[i]] = list_str[i]
                    s.add(list_str[i])
                else:
                    return False
        return True
