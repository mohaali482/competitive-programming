class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target in nums:
            return 1
        mini = 10**5 + 1
        ps = [nums[0]]
        for i in range(1, len(nums)):
            ps.append(ps[-1] + nums[i])

        if ps[-1] == target:
            return len(nums)

        for i in range(len(ps)):
            if ps[i] >= target:
                mini = min(mini, (i+1))

        i = 0
        j = 1

        while i < j:
            if j == len(nums):
                break
            if ps[j] - ps[i] >= target:
                mini = min(mini, (j-i))
                i += 1

            else:
                j += 1
        if mini != 10**5 + 1:
            return mini

        return 0
