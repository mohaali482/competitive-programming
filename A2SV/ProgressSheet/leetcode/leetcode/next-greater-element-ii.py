class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        ans = [-1] * n
        for i in range(n*2):
            while stack and stack[-1][1] < nums[i%n]:
                idx, _ = stack.pop()
                ans[idx] = nums[i%n]
            stack.append((i%n, nums[i%n]))
        
        return ans
