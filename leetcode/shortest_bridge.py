class Solution:
    movement = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def isBound(self, grid: List[List[int]], point: Tuple[int]) -> bool:
        if point[0] < 0 or point[0] >= len(grid):
            return False
        if point[1] < 0 or point[1] >= len(grid[0]):
            return False
        
        return True
    
    def getNeighbors(self, grid: List[List[int]], point: Tuple[int]) -> List[Tuple[int]]:
        neighbors = []
        for x, y in self.movement:
            newPoint = (x + point[0], y + point[1])
            if self.isBound(grid, newPoint) and grid[newPoint[0]][newPoint[1]] and newPoint not in self.visited:
                neighbors.append(newPoint)
            
        return neighbors
    
    def getNeighborsAll(self, grid: List[List[int]], point: Tuple[int]) -> List[Tuple[int]]:
        neighbors = []
        for x, y in self.movement:
            newPoint = (x + point[0], y + point[1])
            if self.isBound(grid, newPoint) and newPoint not in self.visited:
                neighbors.append(newPoint)
            
        return neighbors

    def getLands(self, grid: List[List[int]], point: Tuple[int]):
        self.visited.add(point)
        for neighbor in self.getNeighbors(grid, point):
            self.getLands(grid, neighbor)

    def shortestBridge(self, grid: List[List[int]]) -> int:
        self.visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    self.getLands(grid, (i, j))
                    break
            if self.visited:
                break

        ans = 0
        queue = deque(self.visited)
        while queue:
            for i in range(len(queue)):
                x, y = queue.popleft()
                for newX, newY in self.getNeighborsAll(grid, (x, y)):
                    if grid[newX][newY]:
                        return ans
                    queue.append((newX, newY))
                    self.visited.add((newX, newY))
            ans += 1
        
        return ans