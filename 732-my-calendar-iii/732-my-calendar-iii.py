from sortedcontainers import SortedDict

class MyCalendarThree:

    def __init__(self):
        self.d = SortedDict()

    def book(self, start: int, end: int) -> int:
        if not start in self.d:
            self.d[start] = 0
        if not end in self.d:
            self.d[end] = 0
        self.d[start] += 1
        self.d[end] -= 1
        ans = 0
        cur = 0
        for time, count in self.d.items():
            cur += count
            ans = max(ans, cur)
        return ans


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)