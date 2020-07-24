class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        res = ""
        carry = "0"
        while i > -1 and j > -1:
            sum = int(a[i]) + int(b[j])
            if sum == 2:
                if carry == "1":
                    res += "1"
                else:
                    res += "0"
                    carry = "1"
            elif sum == 1:
                if carry == "1":
                    res += "0"
                else:
                    res += "1"
            else:
                res += carry
                carry = "0"
            i -= 1
            j -= 1
        if i < j:
            i = j
            a = b
        while i > -1:
            if a[i] == "1":
                if carry == "1":
                    res += "0"
                else:
                    res += "1"
            elif carry == "1":
                res += "1"
                carry = "0"
            else:
                res += "0"
            i -= 1

        if carry != "0":
            res += "1"

        return res[::-1]
        # return bin(int(a,2) + int(b,2)).replace("0b","")
