class Solution:
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
            if self.isBound(grid, newPoint) and grid[newPoint[0]][newPoint[1]] == 0 and newPoint not in self.visited:
                neighbors.append(newPoint)
        return neighbors
    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        self.ans = -1
        self.visited = set()
        self.movement = ((1, 0), (1, 1), (1, -1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1))
        queue = deque([(0, 0, 1)])
        while queue:
            x, y, count = queue.popleft()
            if (x, y) in self.visited:
                continue
            if (x, y) == (len(grid)-1, len(grid[0])-1):
                if self.ans != -1:
                    self.ans = min(self.ans, count)
                else:
                    self.ans = count
                continue
            
            self.visited.add((x,y))
            for newX, newY in self.getNeighbors(grid, (x, y)):
                queue.append((newX, newY, count+1))
        return self.ans