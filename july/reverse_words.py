class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split(" ")[::-1]
        wrd = ""
        for i in s:
            if i.strip():
                wrd += i + " "
        return wrd[:-1]
