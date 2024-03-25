class Solution:
    def longestPalindrome(self, s: str) -> int:
        chars = Counter(s)
        ans = 0
        odd = False
        for i in chars:
            if chars[i] % 2 != 0 and not odd:
                ans += 1
                odd = True
            ans += (chars[i]//2)*2
        return ans