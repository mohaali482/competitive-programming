class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = 0
        distance = float("inf")
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while j < k:
                _sum = nums[i] + nums[j] + nums[k]
                current_distance = abs(target - _sum)
                if current_distance < distance:
                    distance = current_distance
                    ans = _sum
                
                if _sum == target:
                    return target
                elif _sum < target:
                    j += 1
                else:
                    k -= 1
        
        return ans