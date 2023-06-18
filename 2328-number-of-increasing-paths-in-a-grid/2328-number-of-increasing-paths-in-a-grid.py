class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        A = defaultdict(list)
        n = len(grid)
        m = len(grid[0])
        mod = 10**9+7
        for i in range(n):
            for j in range(m):
                cur = grid[i][j]
                if i > 0 and grid[i-1][j] < cur:
                    A[(i, j)].append((i-1, j))
                if i < n-1 and grid[i+1][j] < cur:
                    A[(i, j)].append((i+1, j))
                if j > 0 and grid[i][j-1] < cur:
                    A[(i, j)].append((i, j-1))
                if j < m-1 and grid[i][j+1] < cur:
                    A[(i, j)].append((i, j+1))
                    
        @cache
        def dfs(i, j):
            nonlocal A, mod
            ls = A[(i, j)]
            if not ls:
                return 1
            ret = 1 - len(ls)
            for i2, j2 in ls:
                ret = (ret + dfs(i2, j2) + 1) % mod
            return ret
        
        ans = 0
        for i in range(n):
            for j in range(m):
                ans = (ans + dfs(i, j)) % mod
        return ans
        