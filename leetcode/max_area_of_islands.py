class Solution:
    movement = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def isBound(self, grid: List[List[int]], point: Tuple[int]):
        if point[0] >= len(grid) or point[0] < 0:
            return False

        if point[1] >= len(grid[0]) or point[1] < 0:
            return False

        return True

    def getNeighbors(self, grid: List[List[int]], point: Tuple[int]):
        neighbors = []
        for x, y in self.movement:
            newPoint = (point[0] + x, point[1] + y)
            if self.isBound(grid, newPoint) and 1 == grid[newPoint[0]][newPoint[1]]:
                neighbors.append(newPoint)

        return neighbors

    def dfs(self, grid: List[List[int]], point: Tuple[int], area: List[int]):
        if point in self.visited:
            return

        self.visited.add(point)
        area[0] += 1
        for neighbor in self.getNeighbors(grid, point):
            self.dfs(grid, neighbor, area)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        self.visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in self.visited:
                    area = [0]
                    self.dfs(grid, (i, j), area)
                    ans = max(ans, area[0])

        return ans
