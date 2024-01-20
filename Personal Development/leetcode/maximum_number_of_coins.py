class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        total = 0
        i = len(piles) - 2
        while i >= len(piles) / 3:
            total += piles[i]
            i -= 2

        return total
