class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        def permutate(num):
            if len(num) == 0:
                return
            nn = num[:]
            nn.sort()
            if nn in ans:
                return
            ans.append(nn)

            for i in range(len(num)):
                n = num.pop(0)
                permutate(num)
                num.append(n)

        permutate(nums)
        return ans
