class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        n = len(grid)
        if n == 1:
            return 1
        ans = 1
        cur = [(0, 0)]
        d = [[inf] * n for _ in range(n)]
        d[0][0] = 0
        ds = [(-1, 0), (0, -1), (-1, -1), (1, 0), (0, 1), (1, 1), (-1, 1), (1, -1)]
        while cur:
            nxt = []
            ans += 1
            for i, j in cur:
                for di, dj in ds:
                    i2, j2 = i + di, j + dj
                    if 0 <= i2 < n and 0 <= j2 < n and grid[i2][j2] == 0 and ans < d[i2][j2]:
                        if (i2, j2) == (n-1, n-1):
                            return ans
                        d[i2][j2] = ans
                        nxt.append((i2, j2))
            cur = nxt
        return -1