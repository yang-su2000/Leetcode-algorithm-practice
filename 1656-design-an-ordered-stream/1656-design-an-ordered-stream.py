class OrderedStream:

    def __init__(self, n: int):
        self.ls = [None] * n
        self.i = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.ls[idKey-1] = value
        ans = []
        while self.i < len(self.ls) and self.ls[self.i] is not None:
            ans.append(self.ls[self.i])
            self.i += 1
        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)