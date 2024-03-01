class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        current = []
        current_sum = 0
        def solve(idx):
            nonlocal current_sum
            if current_sum == target:
                ans.append(current[:])
                return
            
            seen = set()
            for i in range(idx, len(candidates)):
                if candidates[i] not in seen and current_sum + candidates[i] <= target:
                    current.append(candidates[i])
                    current_sum += candidates[i]
                    solve(i+1)
                    current_sum -= candidates[i]
                    current.pop()
                    seen.add(candidates[i])
        
        solve(0)
        return ans