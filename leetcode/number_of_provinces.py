class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        ans = 0

        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for i in range(len(isConnected)):
                if isConnected[node][i]:
                    dfs(i)

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] and j not in visited:
                    dfs(j)
                    ans += 1

        return ans
