class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        maxi = 0
        b = len(nums)
        for i in range(b//2):
            maxi = max(nums[i] + nums[b-i-1], maxi)
        return maxi
