class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        visited = defaultdict(int)
        visited[0] = 1
        tot = 0
        ans = 0
        for i in range(len(nums)):
            tot += nums[i]
            
            if tot - k in visited:
                ans += visited[tot-k]
            
            visited[tot] += 1
        
        return ans