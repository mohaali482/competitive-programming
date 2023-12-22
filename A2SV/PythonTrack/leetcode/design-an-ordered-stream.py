class OrderedStream:

    def __init__(self, n: int):
        self.list = [""] * n
        self.n = n
        self.ptr = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.list[idKey-1] = value
        result = []
        while self.ptr < self.n:
            if self.list[self.ptr] == "":
                break
            result.append(self.list[self.ptr])
            self.ptr += 1
        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)