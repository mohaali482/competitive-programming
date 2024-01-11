class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        
        if prefix_sum[-1] < target:
            return 0
        
        ans = len(nums)
        left = 0
        right = 1
        _sum = prefix_sum[left]
        if _sum >= target:
            ans = 1
        while right < len(nums):
            _sum = prefix_sum[right]
            while _sum - prefix_sum[left] >= target:
                left += 1
            
            if _sum >= target:
                ans = min(ans, (right - left) + 1)
            
            right += 1
        
        return ans

