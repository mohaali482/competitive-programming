class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        if sum(nums)%p==0:
            return 0
        ans = len(nums)
        k = sum(nums) % p
        total = 0
        
        visited = defaultdict(int)
        visited[0] = -1
        for i in range(len(nums)):
            total = (total + nums[i])%p
            if (total - k) % p in visited:
                ans = min(ans, i - visited[(total - k) % p])
            
            visited[total] = i
        
        if ans >= len(nums):
            return -1
        
        return ans

# class Solution:
#     def minSubarray(self, nums: List[int], p: int) -> int:
#         if sum(nums)%p==0:
#             return 0
#         target = sum(nums) % p
#         dic,n = {0:-1},len(nums)
#         cur,ret = 0,n
#         for i,num in enumerate(nums):
#             cur = (cur+num)%p
#             if dic.get((cur-target)%p) is not None:
#                 ret = min(ret,i-dic.get((cur-target)%p))
#             dic[cur] = i
#         return ret if ret < n else -1