class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 0
        j = len(arr) - 1
        while i < j:
            update = False
            if arr[i] < arr[i+1]:
                i += 1
                update = True
            if arr[j-1] > arr[j]:
                j -= 1
                update = True
            
            if not update:
                return False
            

            
        if i != 0 and j != len(arr) - 1 and i == j:
            return True
        
        return False
            
            