class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        indexes = defaultdict(list)
        two_or_more = set()
        for i in range(len(cards)):
            indexes[cards[i]].append(i)
            if len(indexes[cards[i]]) >= 2:
                two_or_more.add(cards[i])
        
        ans = float("inf")
        for i in two_or_more:
            for j in range(len(indexes[i])-1):
                ans = min(ans, (indexes[i][j+1] - indexes[i][j]) + 1)
        
        if ans == float("inf"):
            return -1
        
        return ans
