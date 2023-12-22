class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = list(s)
        i = 0
        while i < len(s):
            if i + 2*k <= len(s):
                ans[i:i+k] = ans[i:i+k][::-1]
                i += 2*k
            elif k <= len(s) - i or len(s) - i < 2*k:
                ans[i:i+k] = ans[i:i+k][::-1]
                break
            else:
                break
        
        return ''.join(ans)
