class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = [1] * (len(nums)+1)
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]
        
        prefix = [1] * (len(nums)+1)
        for i in range(len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
        
        ans = [1] * len(nums)

        for i in range(len(nums)):
            ans[i] = suffix[i+1] * prefix[i-1]
        
        return ans