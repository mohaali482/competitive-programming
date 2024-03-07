class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect_left(arr, x)

        valid = [max(idx-k, 0), min(idx+k, len(arr)-1)]

        while (valid[1] - valid[0])+1 > k:
            if abs(x - arr[valid[0]]) > abs(x - arr[valid[1]]):
                valid[0] += 1
            else:
                valid[1] -= 1
        
        return arr[valid[0]: valid[1]+1]