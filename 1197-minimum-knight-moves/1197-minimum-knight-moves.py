class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        ans = defaultdict(lambda: inf) # (x, y) -> min
        ans[(0, 0)] = 0
        cur = [(0, 0, 0)]
        d = [(1, 2), (2, 1), (1, -2), (-1, 2), (-2, 1), (2, -1)]
        while cur:
            nxt = []
            for i, j, val in cur:
                if ans[(i, j)] < val:
                    continue
                for di, dj in d:
                    i2, j2 = i + di, j + dj
                    if -3 <= i2 <= x + 3 and -3 <= j2 <= y + 3 and val + 1 < ans[(i2, j2)]:
                        ans[(i2, j2)] = val + 1
                        nxt.append((i2, j2, val + 1))
            cur = nxt
        return ans[(x, y)]