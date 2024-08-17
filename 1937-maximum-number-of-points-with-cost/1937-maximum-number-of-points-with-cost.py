class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        for r in range(1, m):
            row = []
            lmax = 0
            for c in range(n):
                lmax = max(lmax - 1, points[r-1][c])
                row.append(points[r][c] + lmax)
            rmax = 0
            for c in range(n-1, -1, -1):
                rmax = max(rmax - 1, points[r-1][c])
                row[c] = max(row[c], points[r][c] + rmax)
            points[r] = row
        return max(points[-1])