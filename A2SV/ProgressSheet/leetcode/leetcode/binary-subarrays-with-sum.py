class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0
        tot = 0
        visited = defaultdict(int)
        visited[0] = 1
        for i in range(len(nums)):
            tot += nums[i]
            if tot - goal in visited:
                ans += visited[tot-goal]
            
            visited[tot] += 1
        
        return ans
