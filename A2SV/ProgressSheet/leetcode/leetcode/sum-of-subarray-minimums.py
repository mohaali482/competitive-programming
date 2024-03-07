class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        ans = 0

        stack = []
        for idx, val in enumerate(arr):
            while stack and stack[-1][1] > val:
                j, m = stack.pop()
                left = j - stack[-1][0] if stack else j+1
                right = idx - j
                ans += (m * left * right) % mod
                ans %= mod
                
            
            stack.append((idx, val))
        
        for i in range(len(stack)):
            j, m = stack[i]
            left = j - stack[i-1][0] if i > 0 else j+1
            right = len(arr) - j
            ans += (m * left * right) % mod
            ans %= mod
        return ans