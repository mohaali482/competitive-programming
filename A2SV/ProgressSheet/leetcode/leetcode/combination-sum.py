class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        current = []
        _sum = 0
        candidates.sort()
        def solve(idx):
            nonlocal _sum
            if _sum == target:
                ans.append(current[:])
                return
            
            for i in range(idx, len(candidates)):
                if _sum + candidates[i] <= target:
                    current.append(candidates[i])
                    _sum += candidates[i]
                    solve(i)
                    _sum -= current.pop()
                else:
                    break
        
        solve(0)
        return ans