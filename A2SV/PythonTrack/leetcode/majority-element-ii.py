class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        l = len(nums) // 3
        for i, v in c.items():
            if v > l:
                yield i