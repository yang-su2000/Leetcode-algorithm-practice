class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        d = Counter()
        d[(startRow, startColumn)] = 1
        ans = 0
        mod = int(1e9+7)
        for _ in range(maxMove):
            d2 = Counter()
            for (x, y), c in d.items():
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    x2, y2 = x + dx, y + dy
                    if 0 <= x2 < m and 0 <= y2 < n:
                        d2[(x2, y2)] = (d2[(x2, y2)] + c) % mod
                    else:
                        ans = (ans + c) % mod
            d = d2
            # print(d)
        return ans