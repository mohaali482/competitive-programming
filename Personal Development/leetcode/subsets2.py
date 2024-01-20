class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        nums_set = {}
        for i in range(len(nums)):
            nums_set[nums[i]] = i

        def dfs(subset, i):
            if i >= len(nums):
                ans.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(subset, i + 1)

            subset.pop()
            i = nums_set[nums[i]]
            dfs(subset, i + 1)

        dfs([], 0)
        return ans
