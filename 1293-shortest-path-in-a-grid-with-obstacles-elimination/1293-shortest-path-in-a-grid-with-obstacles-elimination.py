class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        d = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        # k [(i, j) -> min_steps]
        seen = set()
        q = [((0, 0, 0), 0)] # ((k, i, j), step)
        while q:
            q2 = []
            for t, step in q:
                if t in seen:
                    continue
                seen.add(t)
                ck, i, j = t
                if i == m-1 and j == n-1:
                    return step
                for di, dj in d:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < m and 0 <= nj < n:
                        nk = ck + grid[ni][nj]
                        if nk <= k:
                            q2.append(((nk, ni, nj), step + 1))
            q = q2
        return -1