class Bitset:

    def __init__(self, size: int):
        self.bits = ["0"] * size
        self.flipped_bits = ["1"] * size
        self._sum = 0

    def fix(self, idx: int) -> None:
        if self.bits[idx] == "0":
            self._sum += 1
        self.bits[idx] = "1"
        self.flipped_bits[idx] = "0"


    def unfix(self, idx: int) -> None:
        if self.bits[idx] == "1":
            self._sum -= 1
        self.bits[idx] = "0"
        self.flipped_bits[idx] = "1"

    def flip(self) -> None:
        self.bits, self.flipped_bits = self.flipped_bits, self.bits
        self._sum = len(self.bits) - self._sum

    def all(self) -> bool:
        return self._sum == len(self.bits)

    def one(self) -> bool:
        return self._sum > 0

    def count(self) -> int:
        return self._sum

    def toString(self) -> str:
        return ''.join(self.bits)


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()