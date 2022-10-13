from sortedcontainers import SortedList

class MaxStack:

    def __init__(self):
        self.s = SortedList() # (idx, val)
        self.v = SortedList() # (val, idx)
        self.c = 0
        
    def push(self, x: int) -> None:
        self.s.add((self.c, x))
        self.v.add((x, self.c))
        self.c += 1

    def pop(self) -> int:
        i, val = self.s.pop()
        self.v.remove((val, i))
        return val

    def top(self) -> int:
        return self.s[-1][1]

    def peekMax(self) -> int:
        return self.v[-1][0]

    def popMax(self) -> int:
        val, i = self.v.pop()
        self.s.remove((i, val))
        return val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()