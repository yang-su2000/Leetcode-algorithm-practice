class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        for i in range(1, n):
            for j in range(m):
                val = inf
                for j2 in range(m):
                    if j2 != j:
                        val = min(val, grid[i][j] + grid[i-1][j2])
                grid[i][j] = val
        return min(grid[-1])