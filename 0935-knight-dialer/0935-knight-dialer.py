class Solution:
    def knightDialer(self, n: int) -> int:
        cur = {(0, 0): 1, (0, 1): 1, (0, 2): 1, (1, 0): 1, (1, 1): 1, (1, 2): 1, (2, 0): 1, (2, 1): 1, (2, 2): 1, (3, 1): 1}
        mod = int(1e9+7)
        ds = [(-1, 2), (-2, 1), (-1, -2), (-2, -1), (1, -2), (2, -1), (1, 2), (2, 1)]
        while n > 1:
            n -= 1
            nxt = defaultdict(int)
            for (x, y), val in cur.items():
                for dx, dy in ds:
                    x2, y2 = x + dx, y + dy
                    if (0 <= x2 <= 2 and 0 <= y2 <= 2) or (x2 == 3 and y2 == 1):
                        nxt[(x2, y2)] += val
                        nxt[(x2, y2)] %= mod
            cur = nxt
        return sum(cur.values()) % mod