class RecentCounter:

    def __init__(self):
        self.arr = deque()

    def ping(self, t: int) -> int:
        while self.arr and t - 3000 > self.arr[0]:
            self.arr.popleft()
        self.arr.append(t)
        return len(self.arr)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)