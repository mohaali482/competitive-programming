class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def permutate(arr, choices):
            if len(arr) == len(nums):
                ans.append(arr[:])
                return
            
            for i in range(len(choices)):
                arr.append(choices[i])
                permutate(arr, choices[:i]+choices[i+1:])
                arr.pop()

        permutate([], nums)
        return ans