class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = nums[i] + prefix[i-1]
        
        result = [0] * len(nums)
        result[0] = (prefix[-1] - (nums[0] * (len(nums))))
        for i in range(1, len(nums)):
            result[i] = ((nums[i] * (i)) - prefix[i-1]) + ((prefix[-1] - prefix[i-1]) - (nums[i] * (len(nums) - i)))
        
        return result