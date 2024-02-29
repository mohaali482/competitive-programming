class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        ans = 0
        current = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            if nums[i] > current:
                x = ceil(nums[i]/current)
                ans += x-1
                current = nums[i]//x
            else:
                current = nums[i]
        return ans