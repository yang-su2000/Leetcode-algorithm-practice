class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], dst: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        ds = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        dp = [[-1] * n for _ in range(m)]
        visited = [[False] * n for _ in range(m)]
        pq = [(0, start[0], start[1])]
        while pq:
            d, i, j = heapq.heappop(pq)
            if visited[i][j]:
                continue
            visited[i][j] = True
            for di, dj in ds:
                ed, ei, ej = d, i, j
                while 0 <= ei + di < m and 0 <= ej + dj < n and maze[ei + di][ej + dj] == 0:
                    ei += di
                    ej += dj
                    ed += 1
                if dp[ei][ej] == -1 or dp[ei][ej] > ed:
                    dp[ei][ej] = ed
                    if ei == dst[0] and ej == dst[1]:
                        pq = []
                        break
                    heapq.heappush(pq, (ed, ei, ej))
        return dp[dst[0]][dst[1]]