class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index = {nums[i]: i for i in range(len(nums))}
        for x, y in operations:
            nums[index[x]] = y
            index[y] = index[x]
            index.pop(x)
        
        return nums