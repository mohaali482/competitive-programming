class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            rowCount = Counter(row)
            for item, count in rowCount.items():
                if item.isdigit() and count > 1:
                    return False
        for i in range(9):
            col_counter = set()
            for j in range(9):
                if board[j][i].isdigit():
                    if board[j][i] in col_counter:
                        return False
                    else:
                        col_counter.add(board[j][i])
        boxes = []
        for i in range(0, 9, 3):
            box = []
            for j in range(9):
                for k in range(i, i+3):
                    box.append(board[k][j])
                if len(box) == 9:
                    boxes.append(box)
                    box = []

        for row in boxes:
            rowCount = Counter(row)
            for item, count in rowCount.items():
                if item.isdigit() and count > 1:
                    return False
        return True