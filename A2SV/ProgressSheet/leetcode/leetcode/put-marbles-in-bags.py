class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        array = []
        for i in range(len(weights)-1):
            array.append(weights[i]+weights[i+1])
        array.sort()
        _max = 0
        _min = 0
        for i in range(k-1):
            _min += array[i]
            _max += array[len(weights)-i-2]
        return _max - _min