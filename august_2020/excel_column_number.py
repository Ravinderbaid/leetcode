class Solution:
    def titleToNumber(self, s: str) -> int:
        str_index = 0
        num = 0
        len_str = len(s)
        val = [1, 26, 676, 17576, 456976, 11881376, 308915776]
        while str_index < len_str:
            num += (ord(s[len_str - str_index - 1]) - 64) * val[str_index]
            str_index += 1
        return num
