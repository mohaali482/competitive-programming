class MyCircularDeque:

    def __init__(self, k: int):
        self.list = []
        self.k = k

    @property
    def size(self) -> int:
        return len(self.list)

    def insertFront(self, value: int) -> bool:
        if self.size == self.k:
            return False

        self.list.insert(0, value)
        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.k:
            return False

        self.list.append(value)
        return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False

        self.list.pop(0)
        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False

        self.list.pop()
        return True

    def getFront(self) -> int:
        if self.list:
            return self.list[0]

        return -1

    def getRear(self) -> int:
        if self.list:
            return self.list[-1]

        return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
