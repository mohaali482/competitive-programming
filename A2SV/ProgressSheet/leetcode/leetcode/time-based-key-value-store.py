class TimeMap:

    def __init__(self):
        self.store = defaultdict(dict)
        self.keyRange = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key][timestamp] = value
        self.keyRange[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store or timestamp < self.keyRange[key][0]:
            return ''
        
        time = bisect_right(self.keyRange[key], timestamp)-1
        return self.store[key][self.keyRange[key][time]]

        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)