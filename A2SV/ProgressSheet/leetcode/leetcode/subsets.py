class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        current = []
        def generate(i):
            for i in range(i, len(nums)):
                current.append(nums[i])
                ans.append(current.copy())
                generate(i+1)
                current.pop()
        generate(0)
        return ans