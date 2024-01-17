class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = sum(nums[:k-1])

        i = 0
        j = k-1
        ans = float("-inf")

        while j < len(nums):
            window += nums[j]
            ans = max(ans, window/k)
            window -= nums[i]
            j += 1
            i += 1

        return ans