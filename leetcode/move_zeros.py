class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            i = 0
            j = len(nums)
            counter = 0
            while i < j:
                if nums[i] == 0:
                    nums.append(nums.pop(i))
                    counter += 1
                if nums[i] == 0 and counter < j+1:
                    counter += 1
                    continue
                i += 1
