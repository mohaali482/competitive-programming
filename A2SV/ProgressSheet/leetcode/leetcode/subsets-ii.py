class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        seen = set()
        current = []
        nums.sort()
        def solve(idx):
            ans.append(current[:])
            if idx == len(nums):
                return
            
            seen = set()
            for i in range(idx, len(nums)):
                if nums[i] not in seen:
                    current.append(nums[i])
                    solve(i+1)
                    seen.add(current.pop())
        solve(0)
        return ans
            