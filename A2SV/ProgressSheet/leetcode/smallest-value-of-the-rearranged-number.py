class Solution:
    def smallestNumber(self, num: int) -> int:
        s = str(num)
        if num < 0:
            s = s[1:]
        if len(s) == 1:
            return num
        c = Counter(s)
        zero = c["0"]
        nums = [i for i in c for j in range(c[i]) if i != '0']
        nums.sort()
        if num < 0:
            return int('-' + ''.join(nums[::-1]) + '0' * zero)

        return int(nums[0] + '0' * zero + ''.join(nums[1:]))
