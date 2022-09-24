class MinStack:

    def __init__(self):
        self.s = []
        self.ms = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.ms or self.ms[-1] >= val:
            self.ms.append(val)

    def pop(self) -> None:
        val = self.s.pop()
        if self.ms[-1] == val:
            self.ms.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.ms[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()