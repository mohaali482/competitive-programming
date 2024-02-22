class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, abs(n))
        
        if n%2 == 0:
            first_half = n // 2
            mul = self.myPow(x, first_half)
            return mul * mul
        else:
            first_half = ((n-1) // 2)
            mul = self.myPow(x, first_half)
            return x * mul * mul