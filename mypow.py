class Solution:
    # created a power function
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        temp = self.myPow(x, int(n / 2))
        if n % 2 == 0:
            return temp * temp
        else:
            if n > 0:
                return x * temp * temp
            else:
                return (temp * temp) / x
