class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] != val:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
            
            right += 1
        
        return left