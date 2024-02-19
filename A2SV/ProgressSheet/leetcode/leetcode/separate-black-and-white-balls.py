class Solution:
    def minimumSteps(self, s: str) -> int:
        ones = [0] * len(s)
        tot = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == "0":
                tot += 1
            ones[i] = tot
        
        ans = 0
        for i in range(len(s)-1, 0, -1):
            if ones[i] == ones[i-1]:
                ans += ones[i]
        
        return ans