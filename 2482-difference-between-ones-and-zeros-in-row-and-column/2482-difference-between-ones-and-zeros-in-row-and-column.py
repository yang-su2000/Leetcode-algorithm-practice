class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        r = [0] * m
        c = [0] * n
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    r[i] += 1
                    c[j] += 1
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = 2 * (r[i] + c[j]) - m - n
        return ans