class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        minimum = sum(cookies)
        kids = [0] * k
        cookies.sort(reverse=True)
        def distribute_cookies(current):
            nonlocal minimum
            if current >= len(cookies):
                minimum = min(minimum, max(kids))
                return

            if max(kids) > minimum:
                return

            for i in range(k):
                if cookies[current] + kids[i] > minimum or (i > 0 and kids[i] == kids[i - 1]):
                    continue
                kids[i] += cookies[current]
                distribute_cookies(current+1)
                kids[i] -= cookies[current]
        
        distribute_cookies(0)
        return minimum