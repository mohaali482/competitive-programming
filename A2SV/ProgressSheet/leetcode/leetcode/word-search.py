class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def solve(boardI, boardJ, wordPointer):
            if wordPointer == len(word):
                return True
            if boardJ == len(board[0]) or boardI == len(board):
                return False
            if boardJ < 0 or boardI < 0:
                return False
            if board[boardI][boardJ] == word[wordPointer]:
                char = word[wordPointer]
                board[boardI][boardJ] = ""
                if solve(boardI+1, boardJ, wordPointer+1):
                    return True
                if solve(boardI-1, boardJ, wordPointer+1):
                    return True
                if solve(boardI, boardJ+1, wordPointer+1):
                    return True
                if solve(boardI, boardJ-1, wordPointer+1):
                    return True
                board[boardI][boardJ] = char
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    char = word[0]
                    board[i][j] = ""
                    if solve(i+1, j, 1):
                        return True
                    if solve(i-1, j, 1):
                        return True
                    if solve(i, j+1, 1):
                        return True
                    if solve(i, j-1, 1):
                        return True
                    board[i][j] = char
        
        return False