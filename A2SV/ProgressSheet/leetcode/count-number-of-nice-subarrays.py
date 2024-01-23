class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd = 0

        left = 0
        right = 0
        oddLeft = float("inf")
        oddRight = float("-inf")
        
        ans = 0
        while right < len(nums):
            if nums[right]%2 == 1:
                odd += 1
                if odd <= k:
                    oddRight = max(oddRight, right)
                    oddLeft = min(oddLeft, right)

            if odd > k:
                ans += ((oddLeft - left) + 1) * (((right-1) - (oddRight-1)))
                oddRight = right
                while odd > k:
                    if nums[left]%2 == 1:
                        odd -= 1
                    left += 1
                
                oddLeft = left
                while oddLeft < len(nums):
                    if nums[oddLeft]%2 == 1:
                        break
                    oddLeft += 1
            
            right += 1
        
        
        if odd == k:
            ans += ((oddLeft - left) + 1) * ((right - oddRight))

        return ans
