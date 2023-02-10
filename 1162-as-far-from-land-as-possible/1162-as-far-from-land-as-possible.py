class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        zeros = 0
        ans = -1
        q = []
        d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                else:
                    zeros += 1
        if not zeros:
            return -1
        while q:
            ans += 1
            q2 = []
            for i, j in q:
                for di, dj in d:
                    i2 = i + di
                    j2 = j + dj
                    if 0 <= i2 < n and 0 <= j2 < n and grid[i2][j2] == 0:
                        grid[i2][j2] = 1
                        q2.append((i2, j2))
            q = q2
        return ans