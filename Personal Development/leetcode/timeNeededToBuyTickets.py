class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        counter = 0

        while tickets[k] != 0:
            for i in range(len(tickets)):
                if tickets[k] == 0:
                    break
                if tickets[i] == 0:
                    continue
                tickets[i] -= 1
                counter += 1
        return counter
