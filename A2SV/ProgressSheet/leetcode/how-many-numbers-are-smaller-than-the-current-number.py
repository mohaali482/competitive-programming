class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_num = sorted(nums)
        new_nums = []

        for i in nums:
            new_nums.append(sorted_num.index(i))
        return new_nums