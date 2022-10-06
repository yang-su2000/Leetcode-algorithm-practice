from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.d:
            return ''
        ls = self.d[key]
        if ls[0][0] > timestamp:
            return ''
        l, r = 0, len(ls) - 1
        while l < r:
            mid = (l + r + 1) // 2
            if ls[mid][0] > timestamp:
                r = mid - 1
            else:
                l = mid
        return ls[l][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)