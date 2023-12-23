class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def dfs(nn, c):
            if nn == n:
                return True
            if nn > n or 3**c > n:
                return False
            
            first = dfs(nn + 3**c, c+1)
            if first:
                return True
            second = dfs(nn, c+1)
            if second:
                return True
            
            return False
        return dfs(0, 0)