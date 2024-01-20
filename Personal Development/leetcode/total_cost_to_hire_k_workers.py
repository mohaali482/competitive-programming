class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        first = costs[:candidates]
        last = costs[max(candidates, len(costs) - candidates) :]
        heapq.heapify(first)
        heapq.heapify(last)

        first_index = candidates
        last_index = len(costs) - candidates - 1
        _sum = 0
        for i in range(k):
            if (first and last and first[0] <= last[0]) or (first and not last):
                _sum += heapq.heappop(first)
                if first_index <= last_index:
                    heapq.heappush(first, costs[first_index])
                    first_index += 1
            else:
                _sum += heapq.heappop(last)
                if first_index <= last_index:
                    heapq.heappush(last, costs[last_index])
                    last_index -= 1

        return _sum
