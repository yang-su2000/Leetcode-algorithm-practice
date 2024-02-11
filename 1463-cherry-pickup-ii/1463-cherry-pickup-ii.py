class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dp = {(0, 0, 0, m - 1): grid[0][0] + grid[0][m - 1]}
        ds = [(1, -1), (1, 0), (1, 1)]
        
        def valid(x, y):
            return 0 <= x < n and 0 <= y < m
        
        for i in range(n - 1):
            dp2 = defaultdict(int)
            for (a, b, c, d), val in dp.items():
                for da, db in ds:
                    for dc, dd in ds:
                        a2, b2, c2, d2 = a + da, b + db, c + dc, d + dd
                        if valid(a2, b2) and valid(c2, d2):
                            val2 = val
                            if (a2, b2) == (c2, d2):
                                val2 += grid[a2][b2]
                            else:
                                val2 += grid[a2][b2] + grid[c2][d2]
                            dp2[(a2, b2, c2, d2)] = max(dp2[(a2, b2, c2, d2)], val2)
            dp = dp2
        return max(dp.values())