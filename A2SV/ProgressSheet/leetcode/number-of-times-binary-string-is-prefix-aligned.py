class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        number = [0 for i in range(len(flips))]
        counter = 0
        flipper = {
            0: 1,
            1: 0
        }
        total = 0
        _sum = 0
        for i in range(len(flips)):
            _sum += number[i]
            flip = flips[i]
            number[flip-1] = flipper[number[flip-1]]
        
            if number[flip-1] == 0:
                total -= 1
                if flip-1 <= i:
                    _sum -= 1
            else:
                total += 1
                if flip-1 <= i:
                    _sum += 1

            if _sum == i+1 and total-_sum == 0:
                counter += 1
        
        return counter