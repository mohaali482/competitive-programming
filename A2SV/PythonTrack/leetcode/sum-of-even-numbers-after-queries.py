class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        _sum = 0
        for i in nums:
            if i % 2 == 0:
                _sum += i
        
        ans = [0] * len(nums)
        i = 0
        for val, index in queries:
            if nums[index]%2 == 0:
                _sum -= nums[index]
            nums[index] += val
            if nums[index] % 2 == 0:
                _sum += nums[index]
            
            ans[i] = _sum
            i += 1

        
        return ans