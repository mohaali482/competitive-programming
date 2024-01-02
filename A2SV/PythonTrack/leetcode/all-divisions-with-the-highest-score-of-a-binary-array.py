class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        ans = {}
        i = 0
        _sum = c[1]
        _max = _sum
        ans[-1] = _sum
        while i < len(nums):
            if nums[i] == 0:
                _sum += 1
            else:
                _sum -= 1
            
            ans[i] = _sum
            _max = max(_max, _sum)
            i += 1
        
        return [i+1 for i in ans if ans[i] == _max]