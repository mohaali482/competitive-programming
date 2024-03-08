class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        def find(divisor):
            current = 0
            for num in nums:
                current += ceil(num/divisor)
            
            return current

        best = right
        while left <= right:
            mid = left + (right-left)//2
            _sum = find(mid)
            if _sum <= threshold:
                right = mid - 1
                best = mid
            else:
                left = mid + 1
        
        return best