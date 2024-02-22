class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        total = 0
        for idx, val in enumerate(tickets):
            total += min(tickets[k], val)
            if idx > k and val >= tickets[k]:
                total -= 1
        return total