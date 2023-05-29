from functools import cmp_to_key as k


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(x, y):
            if int(x + y) > int(y + x):
                return -1
            elif int(x + y) < int(y + x):
                return 1
            return 0

        a = []
        for i in nums:
            a.append(str(i))
        a.sort(key=k(compare))
        return str(int("".join(a)))
