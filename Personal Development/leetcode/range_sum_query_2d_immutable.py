class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.matrix = []
        matr = []
        for i in range(n):
            res = []
            _sum = 0
            for j in range(m):
                _sum += matrix[i][j]
                res.append(_sum)
            matr.append(res)
        self.matrix.append(matr[0])
        for i in range(1, n):
            res = []
            for j in range(m):
                res.append(self.matrix[i-1][j] + matr[i][j])
            self.matrix.append(res)


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.matrix[row2][col2]
        if col1 > 0:
            cur = self.matrix[row2][col1-1]
        else:
            cur = 0
        if row1 > 0:
            cur2 = self.matrix[row1-1][col2]
        else:
            cur2 = 0
        if row1 > 0 and col1 > 0:
            cur3 = self.matrix[row1-1][col1-1]
        else:
            cur3 = 0
        
        return ans + cur3 - cur - cur2

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)