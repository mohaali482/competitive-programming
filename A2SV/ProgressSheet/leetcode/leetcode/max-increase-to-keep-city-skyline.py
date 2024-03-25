class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        tGrid = list(zip(*grid))
        
        west = [max(row) for row in grid]
        north = [max(column) for column in tGrid]
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                rowMax = west[i]
                columnMax = north[j]
                current = min(rowMax, columnMax)
                ans += current - grid[i][j]
        
        return ans
