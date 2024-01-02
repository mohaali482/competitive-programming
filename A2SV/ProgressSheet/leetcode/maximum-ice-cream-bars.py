class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = Counter(costs)
        start = float("inf")
        end = 0
        for cost in costs:
            start = min(start, cost)
            end = max(end, cost)
        
        ans = 0
        keys = sorted(count.keys())
        for i in keys:
            amount = count[i] * i
            if amount <= coins:
                ans += count[i]
                coins -= amount
            else:
                amount = coins//i
                ans += amount
                coins -= amount * i
            if coins == 0:
                break

        return ans