class Solution:
    def numberOfWays(self, s: str) -> int:
        zero = one = 0
        for i in s:
            if i == "0":
                zero += 1
            else:
                one += 1

        left_zero = 0
        left_one = 0
        ans = 0
        for i in s:
            if i == "0":
                ans += left_one * (one-left_one)
                left_zero += 1
            else:
                ans += left_zero * (zero-left_zero)
                left_one += 1
        
        return ans
