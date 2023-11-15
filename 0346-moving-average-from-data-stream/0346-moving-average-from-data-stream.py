class MovingAverage:

    def __init__(self, size: int):
        self.ls = [0]
        self.size = size

    def next(self, val: int) -> float:
        sum_ = self.ls[-1] + val
        self.ls.append(sum_)
        if len(self.ls) > self.size:
            sum_ -= self.ls[-self.size-1]
            return sum_ / self.size
        return sum_ / (len(self.ls) - 1)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)