class Solution:
    def fill(self, grid, i, j):
        grid[i][j] = 1
        for di, dj in self.d:
            i2, j2 = i + di, j + dj
            if 0 <= i2 < self.n and 0 <= j2 < self.m and grid[i2][j2] == 0:
                self.fill(grid, i2, j2)
    
    def closedIsland(self, grid: List[List[int]]) -> int:
        self.d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        self.n = len(grid)
        self.m = len(grid[0])
        for i in range(self.n):
            if grid[i][0] == 0:
                self.fill(grid, i, 0)
            if grid[i][self.m-1] == 0:
                self.fill(grid, i, self.m-1)
        for j in range(self.m):
            if grid[0][j] == 0:
                self.fill(grid, 0, j)
            if grid[self.n-1][j] == 0:
                self.fill(grid, self.n-1, j)
        # for row in grid:
        #     print(row)
        ans = 0
        for i in range(1, self.n-1):
            for j in range(1, self.m-1):
                if grid[i][j] == 0:
                    ans += 1
                    self.fill(grid, i, j)
        return ans