class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0 or n == 2:
            return False
        if n == 1:
            return True
        while n >= 3:
            n /= 3
            if int(n) != n:
                return False

        if n == 1:
            return True
        return False
