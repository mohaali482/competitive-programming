class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        current = []
        _sum = 0
        def solve(idx):
            nonlocal _sum
            if _sum == n and len(current) == k:
                ans.append(current[:])
                return

            if len(current) == k:
                return

            for i in range(idx, 10):
                if _sum + i <= n:
                    _sum += i
                    current.append(i)
                    solve(i+1)
                    _sum -= i
                    current.pop()
                else:
                    break
        
        solve(1)
        return ans