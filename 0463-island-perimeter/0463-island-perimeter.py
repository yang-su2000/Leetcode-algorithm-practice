class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0
        dup = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                ans += 4
                for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    i2, j2 = i + di, j + dj
                    if 0 <= i2 < n and 0 <= j2 < m and grid[i2][j2]:
                        ans -= 1
        return ans