class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        d = [(0, -1), (-1, 0), (1, 0), (0, 1)]
        # k [(i, j) -> min_steps]
        steps = [defaultdict(lambda: float('inf')) for _ in range(k + 1)]
        q = [(0, 0, 0, 0)] # (k, i, j, step)
        while q:
            q2 = []
            for ck, i, j, step in q:
                if i == m-1 and j == n-1:
                    return step
                if (i, j) in steps[ck]:
                    continue
                steps[ck][(i, j)] = step
                for di, dj in d:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < m and 0 <= nj < n:
                        nk = ck + grid[ni][nj]
                        if nk <= k:
                            q2.append((nk, ni, nj, step + 1))
            q = q2
        # ans
        # ans = float('inf')
        # for step_d in steps:
        #     ans = min(ans, step_d[(m-1, n-1)])
        # return -1 if ans == float('inf') else ans
        return -1