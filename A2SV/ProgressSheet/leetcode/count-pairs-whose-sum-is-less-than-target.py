class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        tot = 0
        i = 0
        j = 1
        while i < len(nums):
            if nums[i] > 0 and nums[i] >= target:
                break
            if j >= len(nums):
                i += 1
                j = i + 1
                continue
            if nums[i] + nums[j] < target:
                tot += 1
            
            j += 1

        return tot