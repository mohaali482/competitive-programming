class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        _min = 0
        ans = nums[0]
        tot = 0
        for i in range(len(nums)):
            tot += nums[i]
            ans = max(ans, tot - _min)
            _min = min(_min, tot)
        
        return ans