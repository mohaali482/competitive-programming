class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def solve(current, num):
            if len(current) == k:
                ans.append(current.copy())
                return
            
            for i in range(num, n+1):
                current.append(i)
                solve(current, i+1)
                current.pop()
        solve([], 1)
        return ans