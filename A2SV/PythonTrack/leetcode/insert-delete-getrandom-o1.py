class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False

        val_ind = self.dict[val]
        if val_ind == len(self.list) - 1:
            self.list.pop()
            self.dict.pop(val)
        else:
            self.list[val_ind], self.list[-1] = self.list[-1], self.list[val_ind]
            changed_val = self.list[val_ind]
            self.dict[changed_val] = val_ind
            self.list.pop()
            self.dict.pop(val)
        
        return True

    def getRandom(self) -> int:
        ind = int(random.random() * len(self.list))
        return self.list[ind]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()