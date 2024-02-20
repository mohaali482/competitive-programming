class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = (10**9)+7
        if n % 2 == 0:
            even = n // 2
            odd = n // 2
        else:
            even = (n-1) // 2
            odd = (n+1) // 2
        

        return (pow(5, odd, mod) * pow(4, even, mod)) % mod 