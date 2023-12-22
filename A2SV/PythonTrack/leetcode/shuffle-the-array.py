class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        j = n
        i = 0
        while i < n and j < len(nums):
            ans.append(nums[i])
            ans.append(nums[j])
            i += 1
            j += 1
        ans.extend(nums[i:n])
        ans.extend(nums[j:])
        
        return ans