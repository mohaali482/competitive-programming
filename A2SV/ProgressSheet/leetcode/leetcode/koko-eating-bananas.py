class Solution:
    def getTime(self, piles: List[int], speed: int) -> int:
        time = 0
        for pile in piles:
            if speed > pile:
                time += 1
            else:
                time += ceil(pile/speed)
        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        best = right

        while left < right:
            mid = left + (right-left)//2
            time = self.getTime(piles, mid)
            if time > h: # takes too much time for this speed
                left = mid+1
            else: # takes too little time for this speed:
                best = mid
                right = mid
        
        return right