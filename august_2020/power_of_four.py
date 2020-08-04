class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 1 or num == 4:
            return True
        if num < 4:
            return False
        binfour = bin(num).replace("0b", "")
        len_binfour = len(binfour)
        if len_binfour % 2:
            if binfour[-(len_binfour - 3) :] == "0" * (len_binfour - 3):
                num = num >> (len_binfour - 3)
                if num == 4:
                    return True
        return False
