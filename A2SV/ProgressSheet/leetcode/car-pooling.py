class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_len = float("-inf")
        for trip in trips:
            max_len = max(max_len, trip[-1])
        
        total = [0] * (max_len+2)
        for trip in trips:
            num, _from, _to = trip
            total[_from] += num
            total[_to] -= num
        
        for i in range(1, len(total)):
            total[i] = total[i-1] + total[i]

        for i in range(len(total)):
            if total[i] > capacity:
                return False
        return True