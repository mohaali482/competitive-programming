class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_t_r = []
        r_t_l = []
        length = len(nums) - 1
        for i in range(length + 1):
            if l_t_r:
                l_t_r.append(nums[i] + l_t_r[-1])
            else:
                l_t_r.append(nums[0])

            if r_t_l:
                r_t_l.insert(0, nums[length - i] + r_t_l[0])
            else:
                r_t_l.append(nums[-1])

        for i in range(length + 1):
            if l_t_r[i] == r_t_l[i]:
                return i
        return -1
