class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        maxi = 0
        counter = 0
        while j < len(nums):
            if nums[j] == 0:
                counter += 1

            if counter > k:
                counter -= 1
                maxi = max(maxi, (j) - i)
                if i < len(nums) and nums[i] == 0:
                    counter -= 1
                i += 1
                continue

            j += 1
        else:
            if counter <= k:
                maxi = max(maxi, (j) - i)

        return maxi
