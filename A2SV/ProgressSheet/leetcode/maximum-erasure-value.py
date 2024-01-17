class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        left = 0
        right = 1
        counter[nums[left]] += 1
        _sum = nums[left]
        ans = _sum
        while right < len(nums):
            counter[nums[right]] += 1
            _sum += nums[right]

            while counter[nums[right]] == 2:
                counter[nums[left]] -= 1
                _sum -= nums[left]
                left += 1
            
            ans = max(ans, _sum)
            right += 1
        
        return ans