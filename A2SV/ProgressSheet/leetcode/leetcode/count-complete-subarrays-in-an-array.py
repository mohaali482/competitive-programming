class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total = len(set(nums))
        window = defaultdict(int)
        ans = 0
        left = 0
        right = 0
        while len(window) < total-1:
            window[nums[right]] += 1
            right += 1
        
        while right < len(nums):
            window[nums[right]] += 1
            while len(window) == total:
                ans += len(nums) - right
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    window.pop(nums[left])
                left += 1
            
            right += 1
        
        return ans

