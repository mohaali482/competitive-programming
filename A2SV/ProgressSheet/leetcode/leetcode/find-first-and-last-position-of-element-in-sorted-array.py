class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ansLeft = len(nums)
        ansRight = -1

        left = 0
        right = len(nums)-1

        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                ansLeft = min(mid, ansLeft)
                right = mid-1
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                ansRight = max(mid, ansRight)
                left = mid+1
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        if ansRight == -1:
            return [-1, -1]
        return [ansLeft, ansRight]