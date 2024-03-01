class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        current = []
        def generate(idx):
            ans.append(current[:])
            for i in range(idx, len(nums)):
                current.append(nums[i])
                generate(i+1)
                current.pop()
        generate(0)
        return ans