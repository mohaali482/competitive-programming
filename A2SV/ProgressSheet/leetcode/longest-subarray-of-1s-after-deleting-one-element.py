class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero_counter = 0
        left = 0
        right = 1
        if nums[left] == 0:
            zero_counter += 1

        ans = 0
        while right < len(nums):
            if nums[right] == 0:
                zero_counter += 1
            
            while zero_counter > 1:
                if nums[left] == 0:
                    zero_counter -= 1
                
                left += 1

            ans = max(ans, (right - left))
            right += 1
        
        return ans