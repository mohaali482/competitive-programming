class DataStream:
    def __init__(self, value: int, k: int):
        self.value = value
        self.list = deque()
        self.k = k

    def consec(self, num: int) -> bool:
        if num == self.value:
            self.list.append(num)
            if len(self.list) == self.k:
                return True
            elif len(self.list) > self.k:
                self.list.pop()
                return True
        else:
            self.list = deque()
        return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
