class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ans = {i: set() for i in range(1, n + 1)}
        ans2 = set([i for i in range(1, n + 1)])
        for i in trust:
            a, b = i
            ans[b].add(a)
            if a in ans2:
                ans2.remove(a)

        if ans2:
            judge = ans2.pop()
            if len(ans[judge]) != n - 1:
                return -1
            return judge
        else:
            return -1
