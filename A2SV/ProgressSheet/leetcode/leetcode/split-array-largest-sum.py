class Solution:
    def getK(self, nums: List[int], size: int) -> int:
        buckets = 0
        current = 0
        for num in nums:
            if num + current > size:
                buckets += 1
                current = num
            else:
                current += num
        
        return buckets + 1

    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        while left <= right:
            mid = left + (right-left)//2
            current = self.getK(nums, mid)
            if current <= k:
                right = mid-1
            else:
                left = mid+1
        
        return left