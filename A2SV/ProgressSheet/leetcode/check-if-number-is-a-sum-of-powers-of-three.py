class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        x = int(n**(1/3))
        while x > -1 and n > 0:
            if 3**x <= n:
                n -= 3**x
            x -= 1

        return n == 0