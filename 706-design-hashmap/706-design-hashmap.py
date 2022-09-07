class MyHashMap:

    def __init__(self):
        self.hash = 100
        self.d = [[] for _ in range(self.hash)]

    def put(self, key: int, value: int) -> None:
        ls = self.d[key % self.hash]
        for i, (k, v) in enumerate(ls):
            if k == key:
                ls[i] = (key, value)
                return
        ls.append((key, value))

    def get(self, key: int) -> int:
        ls = self.d[key % self.hash]
        for k, v in ls:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        ls = self.d[key % self.hash]
        for i, (k, v) in enumerate(ls):
            if k == key:
                ls.pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)