class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        counter = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                nums[j] = 101
            else:
                counter += 1
                i = j
            j += 1
        nums.sort()
        return counter