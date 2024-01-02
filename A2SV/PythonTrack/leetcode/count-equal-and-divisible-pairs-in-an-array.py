class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        new_nums = [(nums[i], i) for i in range(len(nums))]
        new_nums.sort()
        counter = 0
        i = 0
        for i in range(len(new_nums)):
            num, index = new_nums[i]
            for j in range(i+1, len(new_nums)):
                num2, index2 = new_nums[j]
                if num2 != num:
                    break
                if (index * index2) % k == 0:
                    counter += 1

        return counter 