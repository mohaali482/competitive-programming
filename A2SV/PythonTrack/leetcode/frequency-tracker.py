class FrequencyTracker:

    def __init__(self):
        self.numbers = defaultdict(int)
        self.freq = defaultdict(int)

    def add(self, number: int) -> None:
        if number in self.numbers:
            self.freq[self.numbers[number]] -= 1
        self.numbers[number] += 1
        self.freq[self.numbers[number]] += 1

    def deleteOne(self, number: int) -> None:
        if number in self.numbers and self.numbers[number] > 0:
            self.freq[self.numbers[number]] -= 1
            self.numbers[number] -= 1
            self.freq[self.numbers[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return self.freq[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)