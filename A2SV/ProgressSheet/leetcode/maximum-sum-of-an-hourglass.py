class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        _sum = sum(grid[0][:3]) + grid[1][1] + sum(grid[2][:3])
        _max = _sum
        top_left_corner_i = 0
        top_left_corner_j = 0
        top_right_corner_i = 0
        top_right_corner_j = 2
        
        middle_i = 1
        middle_j = 1
        
        bottom_left_corner_i = 2
        bottom_left_corner_j = 0
        bottom_right_corner_i = 2
        bottom_right_corner_j = 2

        while bottom_right_corner_i < len(grid) and bottom_left_corner_i < len(grid):
            _sum -= (
                grid[top_left_corner_i][top_left_corner_j] +
                grid[middle_i][middle_j] +
                grid[bottom_left_corner_i][bottom_left_corner_j]
            )
            
            top_left_corner_j += 1
            top_right_corner_j += 1
            
            middle_j += 1
            
            bottom_left_corner_j += 1
            bottom_right_corner_j += 1


            if top_right_corner_j == len(grid[0]):
                _sum = 0
                top_left_corner_i += 1
                top_left_corner_j = 0
                top_right_corner_i += 1
                top_right_corner_j = 2
                
                middle_i += 1
                middle_j = 1
                
                bottom_left_corner_i += 1
                bottom_left_corner_j = 0
                bottom_right_corner_i += 1
                bottom_right_corner_j = 2
 
                if bottom_right_corner_i == len(grid):
                    break
                else:
                    _sum = sum(grid[top_left_corner_i][:3]) + grid[middle_i][1] + sum(grid[bottom_left_corner_i][:3])
                    _max = max(_max, _sum)
                    continue

            _sum += (
                grid[top_right_corner_i][top_right_corner_j] +
                grid[middle_i][middle_j] +
                grid[bottom_right_corner_i][bottom_right_corner_j]
            )

            _max = max(_sum, _max)
        
        return _max
