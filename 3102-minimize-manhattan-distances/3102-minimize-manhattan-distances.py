from sortedcontainers import SortedList

class Solution:
    def minimumDistance(self, points: List[List[int]]) -> int:
        n = len(points)
        xs = SortedList((x - y, idx) for idx, (x, y) in enumerate(points))
        ys = SortedList((x + y, idx) for idx, (x, y) in enumerate(points))
        ans = inf
        for idx in range(n):
            x, y = points[idx]
            x, y = x - y, x + y
            xs.remove((x, idx))
            ys.remove((y, idx))
            ans = min(ans, max(xs[-1][0] - xs[0][0], ys[-1][0] - ys[0][0]))
            xs.add((x, idx))
            ys.add((y, idx))
        return ans
        