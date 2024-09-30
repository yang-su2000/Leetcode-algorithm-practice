class CustomStack:

    def __init__(self, maxSize: int):
        self.st = []
        self.size = maxSize

    def push(self, x: int) -> None:
        if len(self.st) < self.size:
            self.st.append(x)

    def pop(self) -> int:
        if not self.st:
            return -1
        return self.st.pop()

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, len(self.st))):
            self.st[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)