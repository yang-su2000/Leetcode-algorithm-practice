class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time = 0
        fresh = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                status = grid[i][j]
                if status == 2:
                    q.append((i, j))
                elif status == 1:
                    fresh += 1
        while q and fresh:
            time += 1
            l = len(q)
            for _ in range(l):
                i, j = q.popleft()
                if i and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    q.append((i-1, j))
                    fresh -= 1
                if i + 1 < m and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    q.append((i+1, j))
                    fresh -= 1
                if j and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    q.append((i, j-1))
                    fresh -= 1
                if j + 1 < n and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    q.append((i, j+1))
                    fresh -= 1
        return time if fresh == 0 else -1