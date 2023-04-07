class Solution:
    def dfs(self, grid, i, j):
        grid[i][j] = 0
        for di, dj in self.d:
            i2, j2 = i + di, j + dj
            if 0 <= i2 < len(grid) and 0 <= j2 < len(grid[0]) and grid[i2][j2] == 1:
                self.dfs(grid, i2, j2)
    
    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(len(grid)):
            if grid[i][0]:
                self.dfs(grid, i, 0)
            if grid[i][-1]:
                self.dfs(grid, i, len(grid[0]) - 1)
        for j in range(len(grid[0])):
            if grid[0][j]:
                self.dfs(grid, 0, j)
            if grid[-1][j]:
                self.dfs(grid, len(grid) - 1, j)
        return sum([sum(row) for row in grid])