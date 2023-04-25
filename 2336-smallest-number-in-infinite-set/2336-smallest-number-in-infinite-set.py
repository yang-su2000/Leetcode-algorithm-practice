class SmallestInfiniteSet:

    def __init__(self):
        self.lo = 1
        self.ls = [True] * 1002

    def popSmallest(self) -> int:
        ret = self.lo
        self.ls[ret] = False
        while not self.ls[self.lo]:
            self.lo += 1
        return ret

    def addBack(self, num: int) -> None:
        self.ls[num] = True
        self.lo = min(self.lo, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)