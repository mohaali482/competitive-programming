class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero = 0
        left = 0
        right = 1
        if nums[left] == 0:
            zero += 1
        ans = 0
        if zero == 0:
            ans = 1
        elif k > 0:
            ans = 1
        while right < len(nums):
            if nums[right] == 0:
                zero += 1

            while zero > k:
                if nums[left] == 0:
                    zero -= 1

                left += 1

            ans = max(ans, (right - left) + 1)
            right += 1

        return ans 