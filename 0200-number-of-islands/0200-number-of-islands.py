class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ans = 0
        for i, row in enumerate(grid):
            for j, item in enumerate(row):
                if item == '1':
                    ans += 1
                    self.spread(i, j, grid)
        return ans
    
    def spread(self, i, j, grid):
        
        grid[i][j] = '0'
        if i > 0 and grid[i-1][j] == '1':
            self.spread(i-1, j, grid)
        if i < len(grid) - 1 and grid[i+1][j] == '1':
            self.spread(i+1, j, grid)
        if j > 0 and grid[i][j-1] == '1':
            self.spread(i, j-1, grid)
        if j < len(grid[0]) - 1 and grid[i][j+1] == '1':
            self.spread(i, j+1, grid)