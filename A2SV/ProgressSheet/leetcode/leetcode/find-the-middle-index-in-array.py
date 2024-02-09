class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        suffix = [nums[-1]]
        for i in range(len(nums)-2, -1, -1):
            suffix.append(suffix[-1]+nums[i])
        
        suffix.reverse()
        
        for i in range(len(nums)):
            if prefix[i] == suffix[i]:
                return i
            
        return -1