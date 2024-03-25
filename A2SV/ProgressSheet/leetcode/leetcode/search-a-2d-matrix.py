class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = [row[0] for row in matrix]
        row_index = bisect_left(rows, target)
        if row_index < len(rows) and rows[row_index] == target:
            return True


        row_index -= 1
        target_index = bisect_left(matrix[row_index], target)
        if target_index < len(matrix[0]) and matrix[row_index][target_index] == target:
            return True
        
        return False