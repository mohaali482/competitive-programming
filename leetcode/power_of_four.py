class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0 or n == 2 or n == 3:
            return False
        if n == 1:
            return True
        while n >= 4:
            n /= 4
            if int(n) != n:
                return False

        if n == 1:
            return True
        return False
