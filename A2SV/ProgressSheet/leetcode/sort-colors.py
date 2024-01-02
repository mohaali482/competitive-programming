class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countSort = Counter(nums)
        j = 0
        for i in range(3):
            if i in countSort:
                nums[j: j+countSort[i]] = [i] * countSort[i]
                j += countSort[i]