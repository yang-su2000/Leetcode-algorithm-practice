class MyQueue:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        if self.q2:
            return self.q2.pop()
        self.q1toq2()
        return self.q2.pop()

    def peek(self) -> int:
        if self.q2:
            return self.q2[-1]
        self.q1toq2()
        return self.q2[-1]

    def empty(self) -> bool:
        return not (self.q1 or self.q2)
    
    def q1toq2(self):
        while self.q1:
            self.q2.append(self.q1.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()