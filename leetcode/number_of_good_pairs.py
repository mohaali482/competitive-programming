class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num = {}
        for i in nums:
            num[i] = nums.count(i)

        counter = 0
        for _, values in num.items():
            if values > 0:
                counter += (values - 1)*values//2

        return counter
