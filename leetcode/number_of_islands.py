class Solution:
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def inBound(self, newI, newJ, grid):
        if newI >= len(grid) or newI < 0:
            return False

        if newJ >= len(grid[0]) or newJ < 0:
            return False

        return True

    def dfs(self, i, j, grid, visited):
        visited.add((i, j))

        for x, y in self.move:
            newI = i + x
            newJ = j + y

            if self.inBound(newI, newJ, grid):
                if (newI, newJ) not in visited:
                    if grid[newI][newJ] == "1":
                        self.dfs(newI, newJ, grid, visited)

    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = set()
        ans = 0
        for i in range(n):
            for j in range(m):
                if (i, j) not in visited and grid[i][j] == "1":
                    self.dfs(i, j, grid, visited)
                    ans += 1
        return ans
