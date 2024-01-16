class RandomizedSet:

    def __init__(self):
        
        self.map = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        
        if val in self.map:
            return False
        self.map[val] = len(self.lst)
        self.lst.append(val)
        return True

    def remove(self, val: int) -> bool:
        
        if val in self.map:
            i = self.map[val]
            last_val = self.lst[-1]
            j = self.map[last_val]
            self.map[val], self.map[last_val] = j, i
            self.lst[i], self.lst[j] = last_val, val
            del self.map[val]
            self.lst.pop()
            return True
        return False
        
    def getRandom(self) -> int:
        
        return random.choice(self.lst)
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()