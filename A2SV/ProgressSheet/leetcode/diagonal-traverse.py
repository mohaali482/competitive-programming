class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        n = len(mat)
        m = len(mat[0])
        turn = True
        x = 0
        y = 0
        while x < n and y < m:
            temp = []
            newX = x
            newY = y
            while newX < n and newY > -1:
                temp.append(mat[newX][newY])
                newX += 1
                newY -= 1
            
            if turn:
                ans.extend(temp[::-1])
            else:
                ans.extend(temp)
            
            turn = not turn
            y += 1
            if y == m and x == n:
                break
            if y == m:
                y -= 1
                x += 1

    
        return ans