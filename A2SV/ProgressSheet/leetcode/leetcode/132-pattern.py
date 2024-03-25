class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        n = len(nums)
        stack = []
        third = float("-inf")
        for i in range(n-1, -1, -1):
            if nums[i] < third:
                return True
            while stack and nums[i] > stack[-1]:
                third = stack.pop()
            stack.append(nums[i])
        return False