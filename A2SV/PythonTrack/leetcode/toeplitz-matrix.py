class Solution:
    def check(self, row1, row2) -> bool:
        for i in range(len(row1)-1):
            if row1[i] != row2[i+1]:
                return False
        
        return True

    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(len(matrix)-1):
            if not self.check(matrix[i], matrix[i+1]):
                return False

        return True