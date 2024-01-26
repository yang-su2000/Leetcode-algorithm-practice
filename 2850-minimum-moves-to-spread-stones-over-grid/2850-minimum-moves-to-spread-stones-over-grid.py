class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        c0 = []
        c1 = []
        for a in range(3):
            for b in range(3):
                if grid[a][b] == 0:
                    c0.append((a, b))
                elif grid[a][b] > 1:
                    for _ in range(grid[a][b] - 1):
                        c1.append((a, b))
        ans = inf
        for c in permutations(c1):
            cur = 0
            for (x1, y1), (x2, y2) in zip(c, c0):
                cur += abs(x1 - x2) + abs(y1 - y2)
            ans = min(ans, cur)
        return ans