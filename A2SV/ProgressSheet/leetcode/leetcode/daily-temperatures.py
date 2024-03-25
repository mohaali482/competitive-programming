class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                temp = stack.pop()
                ans[temp[0]] = i - temp[0]
            stack.append((i, temperatures[i]))

        return ans

with open('user.out', 'w') as f:
    for case in map(loads, stdin):
        f.write(f"[{','.join([str(x) for x in Solution().dailyTemperatures(case)])}]\n")
exit()