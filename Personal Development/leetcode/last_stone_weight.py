class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-i for i in stones]
        heapq.heapify(neg_stones)
        while len(neg_stones) > 1:
            x = heapq.heappop(neg_stones)
            y = heapq.heappop(neg_stones)
            res = -abs(y - x)
            if res != 0:
                neg_stones.append(-abs(y - x))
            heapq.heapify(neg_stones)

        if neg_stones:
            return -neg_stones[0]

        return 0
