# One way to solve with strip
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         s = s.strip()
#         c = len(s) - 1
#         if not s:
#             return 0
#         while c >= 0 and s[c].isalpha():
#             c -= 1
#         return len(s) - c - 1


# Another and better way to solve without strip.


class Solution:
    """
    Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

    If the last word does not exist, return 0.

    Note: A word is defined as a maximal substring consisting of non-space characters only.

    Example:

    Input: "Hello World"
    Output: 5
    """

    def lengthOfLastWord(self, s: str) -> int:
        c = start = len(s)
        flag = 0
        while c > 0:
            if s[c - 1].isalpha():
                if flag == 0:
                    start = c
                    flag = 1
            else:
                if flag:
                    return start - c
            c -= 1
        if flag:
            return start
        else:
            return 0
