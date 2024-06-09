class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(x,y,direction):
            if x < 0 or x>= m or y < 0 or y >=len(grid[0]) or grid[x][y] !=1:
                return
            grid[x][y]=0
            path.append(direction)
            dfs(x+1, y, 'D')
            dfs(x-1, y, 'U')
            dfs(x, y+1, 'R')
            dfs(x, y-1, 'L')
            path.append('B')

        distinct_islands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    path = []
                    dfs(i,j,'S')
                    distinct_islands.add(tuple(path))
        return len(distinct_islands)