class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        d = {(row, column): 1.}
        ds = [(-2, -1), (-1, -2), (-1, 2), (2, -1), (-2, 1), (1, -2), (1, 2), (2, 1)]
        for _ in range(k):
            d2 = defaultdict(float)
            for (x, y), p in d.items():
                for dx, dy in ds:
                    x2, y2 = x + dx, y + dy
                    if 0 <= x2 < n and 0 <= y2 < n:
                        d2[(x2, y2)] += p / 8
            d = d2
        return sum(d.values())