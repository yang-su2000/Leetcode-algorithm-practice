class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = not grid[i][j]
        ans = (1 << (n - 1)) * m
        for j, b in zip(range(1, n), range(n-2, -1, -1)):
            count = 0
            for i in range(m):
                count += grid[i][j]
            ans += (1 << b) * max(count, m - count)
        return ans