class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        set_nums = set(nums)
        new_nums = set()
        for i in set_nums:
            new_nums.add((nums.count(i), i))

        new_nums = list(new_nums)
        new_nums.sort(reverse=True)
        x = []
        for i in range(k):
            x.append(new_nums[i][1])

        return x
