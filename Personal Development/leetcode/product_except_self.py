class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        z = nums.count(0)
        if z > 1:
            return [0 for i in range(len(nums))]
        elif z == 1:
            if not nums[0] == 0:
                ps = [nums[0]]
                for i in range(1, len(nums)):
                    if nums[i] != 0:
                        ps.append(ps[-1] * nums[i])
                    else:
                        zindex = i
            else:
                ps = [nums[1]]
                zindex = 0
                for i in range(2, len(nums)):
                    ps.append(ps[-1] * nums[i])

            res = [0 for i in range(len(nums))]
            res[zindex] = ps[-1]
            return res

        ps = [nums[0]]
        for i in range(1, len(nums)):
            ps.append(ps[-1] * nums[i])

        res = [ps[-1]//i for i in nums]

        return res
