class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        _sum = 0
        start = (0, 0)
        visited = set()
        while start[0] < len(mat) and start[1] < len(mat):
            if start not in visited:
                _sum += mat[start[0]][start[1]]
            
            visited.add(start)
            start = start[0] + 1, start[1] + 1

        start = (0, len(mat)-1)
        while start[0] > -1 and start[1] > -1:
            if start not in visited:
                _sum += mat[start[0]][start[1]]
            
            visited.add(start)
            start = start[0] + 1, start[1] - 1

        return _sum