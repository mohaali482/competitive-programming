class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        low, high = 1, x
        ans = 1
        while low <= high:
            mid = low + (high-low)//2
            sq = mid * mid
            if sq > x:
                high = mid - 1
            elif sq < x:
                ans = max(ans, mid)
                low = mid + 1
            else:
                return mid
        
        return ans

