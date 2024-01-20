class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = float("inf")
        children = [0] * k

        def distribute(i):
            nonlocal ans, children
            _max = max(children)
            if i == len(cookies):
                ans = min(ans, _max)
                return
            if ans < _max:
                return

            for j in range(k):
                children[j] += cookies[i]
                distribute(i + 1)
                children[j] -= cookies[i]

        distribute(0)

        return ans
