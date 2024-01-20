class Solution:
    movement = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def isBound(self, grid: List[List[int]], point: Tuple[int]):
        if point[0] >= len(grid) or point[0] < 0:
            return False

        if point[1] >= len(grid[0]) or point[1] < 0:
            return False

        return True

    def getNeighbors(self, grid: List[List[int]], point: Tuple[int]):
        for x, y in self.movement:
            newPoint = (point[0] + x, point[1] + y)
            if self.isBound(grid, newPoint) and 1 == grid[newPoint[0]][newPoint[1]]:
                yield newPoint

    def dfs(self, grid: List[List[int]], point: Tuple[int]):
        if grid[point[0]][point[1]] == 0:
            return 0
        grid[point[0]][point[1]] = 0
        ans = 1
        for neighbor in self.getNeighbors(grid, point):
            ans += self.dfs(grid, neighbor)
        return ans

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans = max(ans, self.dfs(grid, (i, j)))

        return ans
