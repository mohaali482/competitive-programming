class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        arr = [["." for i in range(n)]for i in range(n)]
        ans = []
        def indexIsValid(i, j):
            if i >= n or j >= n:
                return False
            if i < 0 or j < 0:
                return False
            
            return True

        def validate(i, j):
            movement = [
                (-1, 1),  # Up Right
                (-1, 0),  # Up
                (-1, -1), # Up Left
            ]
            for x, y in movement:
                tempI, tempJ = i, j
                while indexIsValid(tempI+x, tempJ+y):
                    tempI, tempJ = tempI+x, tempJ+y
                    if arr[tempI][tempJ] == "Q":
                        return False
            return True


        def find(i, no_of_queen):
            if no_of_queen == n:
                ans.append([''.join(i) for i in arr])
                return 
            if i == n:
                return 
            
            for en in range(n):
                if validate(i, en):
                    arr[i][en] = "Q"
                    find(i+1, no_of_queen+1)
                    arr[i][en] = "."
    
        for j in range(n):
            arr[0][j] = "Q"
            find(1, 1)
            arr[0][j] = "."
    
        return ans