class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        updates = [0] * (len(nums)+1)
        for start, end in requests:
            updates[start] += 1
            updates[end+1] -= 1
        
        for i in range(1, len(nums)):
            updates[i] = updates[i-1] + updates[i]
        
        updates.pop()
        updates.sort()
        nums.sort()
        
        total = 0
        for i in range(len(updates)):
            total += nums[i] * updates[i]
        
        return total % ((10**9)+7)
        