class Solution:
    def fib(self, n: int) -> int:
        a = [0, 1]
        for i in range(2, n+2):
            a.append(a[i-2]+a[i-1])

        return a[n]
