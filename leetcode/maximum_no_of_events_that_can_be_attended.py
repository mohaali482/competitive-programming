class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)

        started = []
        count = 0
        i = 0
        current_day = events[0][0]

        while i < n:
            while i < n and events[i][0] == current_day:
                heapq.heappush(started, events[i][1])
                i += 1

            heapq.heappop(started)
            count += 1
            current_day += 1

            while started and started[0] < current_day:
                heapq.heappop(started)

            if i < n and not started:
                current_day = events[i][0]

        while started:
            if heapq.heappop(started) >= current_day:
                current_day += 1
                count += 1

        return count

        return counter
