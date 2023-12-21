class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        c, j = 1, arr[0]
        for i in range(1, len(arr)):
            if arr[i] == j:
                c += 1
            else:
                c = 1
                j = arr[i]
            
            if c*4 > len(arr):
                return j
        return j