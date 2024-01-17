class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                _sum = nums[i] + nums[j] + nums[k]
                if _sum == 0:
                    ans.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif _sum > 0:
                    k -= 1
                else:
                    j += 1
        return list(ans)