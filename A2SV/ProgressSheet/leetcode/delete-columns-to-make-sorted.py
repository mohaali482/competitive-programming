class Solution:
    def isSorted(self, column: str) -> bool:
        for i in range(1, len(column)):
            if column[i] < column[i-1]:
                return False
        
        return True

    def minDeletionSize(self, strs: List[str]) -> int:
        columns = zip(*strs)
        counter = 0
        for column in columns:
            if not self.isSorted(column):
                counter += 1
        
        return counter