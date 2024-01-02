class Solution:
    direction = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]
    def isValid(self, grid: List[List[int]], point: Tuple[int]) -> bool:
        if point[0] < 0 or point[0] >= len(grid):
            return False
        
        if point[1] < 0 or point[1] >= len(grid[0]):
            return False
        
        if point in self.walls:
            return False
        
        return True
    
    def validate(self, grid: List[List[int]], point: Tuple[int]):
        for x, y in self.direction:
            newPoint = point[0] + x, point[1] + y
            while self.isValid(grid, newPoint) and newPoint not in self.guards:
                grid[newPoint[0]][newPoint[1]] = 0
                newPoint = newPoint[0] + x, newPoint[1] + y

        

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[1 for i in range(n)] for j in range(m)]
        self.guards = set([tuple(guard) for guard in guards])
        self.walls = set([tuple(wall) for wall in walls])
        for guard in self.guards:
            self.validate(grid, guard)
            grid[guard[0]][guard[1]] = 0
        
        for wall in self.walls:
            grid[wall[0]][wall[1]] = 0
        
        _sum = 0
        for row in grid:
            _sum += sum(row)
                
        return _sum
