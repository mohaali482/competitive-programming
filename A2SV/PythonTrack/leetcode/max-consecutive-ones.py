class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        while left < len(nums):
            if nums[left] == 1:
                break
            left += 1
        right = left
        ans = 0
        while right < len(nums):
            if nums[right] != 1:
                ans = max(ans, right - left)
                while right < len(nums):
                    if nums[right] == 1:
                        break
                    right += 1
                left = right
            
            right += 1
        
        return max(ans, right - left)