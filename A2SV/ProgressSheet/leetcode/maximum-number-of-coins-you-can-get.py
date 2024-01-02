class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        print(piles)
        ans = 0
        for j in range(len(piles)-2, (len(piles)//3) - 1, -2):
            ans += piles[j]
        
        return ans