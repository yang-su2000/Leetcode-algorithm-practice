ans = defaultdict(lambda: inf) # (x, y) -> min
ans[(0, 0)] = 0
cur = [(0, 0, 0)]
d = [(-1, -2), (-1, 2), (-2, 1), (-2, -1), (1, 2), (1, -2), (2, 1), (2, -1)]
while cur:
    nxt = []
    for i, j, val in cur:
        if ans[(i, j)] < val:
            continue
        for di, dj in d:
            i2, j2 = i + di, j + dj
            if abs(i2) >= 305 or abs(j2) >= 305:
                continue
            if val + 1 < ans[(i2, j2)]:
                ans[(i2, j2)] = val + 1
                nxt.append((i2, j2, val + 1))
    cur = nxt

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        return ans[(x, y)]