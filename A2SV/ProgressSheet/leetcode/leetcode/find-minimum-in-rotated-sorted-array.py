class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left = 0
        right = len(nums)-1
        best = nums[0]
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] >= best:
                left = mid+1
            else:
                best = nums[mid]
                right = mid-1
        
        return best
