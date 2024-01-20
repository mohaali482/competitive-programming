class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        heap = []
        c = Counter(tasks)
        heap = [-count for count in c.values()]
        heapq.heapify(heap)
        queue = deque()
        time = 0

        while heap or queue:
            time += 1

            if heap:
                current = heapq.heappop(heap) + 1
                if current != 0:
                    queue.append((current, time + n))

            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])

        return time
