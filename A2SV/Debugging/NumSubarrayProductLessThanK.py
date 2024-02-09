from typing import List

class Solution:
        def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
            i, j = 0, 0
            product = 1
            subarrays = 0
            while j < len(nums):
                # Removed the "j < len(nums) - 1" part since it is not needed.
                if product * nums[j] < k:
                    product *= nums[j]
                    j += 1
                elif i < j:
                    subarrays += j - i
                    product //= nums[i]
                    i += 1
                else:
                    i += 1
                    j += 1
            
            # Added a new block to calculate the subarrays between "i" and "j".
            # The formula is (j - i) * (j - i + 1) // 2.
            if i < j:
                tot = j - i
                subarrays += (tot * (tot + 1)) // 2
            
            return subarrays


if __name__ == '__main__':
    assert Solution().numSubarrayProductLessThanK([1, 2, 3, 4], 10) == 7
    assert Solution().numSubarrayProductLessThanK([1, 9, 2, 8, 6, 4, 3], 100) == 16