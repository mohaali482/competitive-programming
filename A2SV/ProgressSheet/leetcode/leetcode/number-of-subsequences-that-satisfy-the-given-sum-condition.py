class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        ans = 0
        nums.sort()
        for i in range(len(nums)):
            difference = bisect_right(nums, target-nums[i])-1
            if difference < i:
                break
            
            ans = (ans + (pow(2, (difference - i), MOD))) % MOD
        
        return ans