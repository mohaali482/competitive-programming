class Solution:
    def isBound(self, board: List[List[str]], node: List[int]) -> bool:
        if node[0] >= len(board) or node[0] < 0:
            return False
        if node[1] >= len(board[0]) or node[1] < 0:
            return False

        return True

    def isBomb(self, board: List[List[str]], node: List[int]) -> bool:
        return board[node[0]][node[1]] == "M"

    def isEmpty(self, board: List[List[str]], node: List[int]) -> bool:
        return board[node[0]][node[1]] == "E"

    def getNumberOfBombs(self, board: List[List[str]], node: List[int]) -> int:
        bombs = 0
        for x, y in self.movement:
            newNode = [node[0] + x, node[1] + y]
            if self.isBound(board, newNode) and self.isBomb(board, newNode):
                bombs += 1

        return bombs

    def dfs(self, board: List[List[str]], node: List[int]):
        if self.isBomb(board, node):
            board[node[0]][node[1]] = "X"
            return

        if self.isEmpty(board, node):
            bombs = self.getNumberOfBombs(board, node)
            if bombs == 0:
                board[node[0]][node[1]] = "B"
                for x, y in self.movement:
                    newNode = (node[0] + x, node[1] + y)
                    if self.isBound(board, newNode) and newNode not in self.visited:
                        self.visited.add(newNode)
                        self.dfs(board, newNode)
            else:
                board[node[0]][node[1]] = str(bombs)
                return

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.visited = set()
        self.movement = [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [0, -1],
            [0, 1],
            [1, -1],
            [1, 0],
            [1, 1],
        ]
        self.visited.add((click[0], click[1]))
        self.dfs(board, click)
        return board
