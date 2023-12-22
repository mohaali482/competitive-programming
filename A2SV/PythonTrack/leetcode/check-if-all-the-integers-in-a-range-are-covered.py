class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        _max = 0
        for _range in ranges:
            _max = max(_range[1], _max)
        if _max < right:
            return False
        prefix = [0 for i in range(_max+2)]
        for x, y in ranges:
            prefix[x] += 1
            prefix[y+1] -= 1
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i] + prefix[i-1]
        
        for i in range(left, right+1):
            if prefix[i] == 0:
                return False
        
        return True