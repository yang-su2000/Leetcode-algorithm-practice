class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        ls = [points[i] + points[j] for i in range(n) for j in range(i+1, n)]
        ans = 0
        for line in ls:
            cur = 0
            dx2, dy2 = line[2] - line[0], line[3] - line[1]
            for p in points:
                dx1, dy1 = p[0] - line[0], p[1] - line[1]
                cur += (dx1 * dy2 == dy1 * dx2)
            ans = max(ans, cur)
        return ans