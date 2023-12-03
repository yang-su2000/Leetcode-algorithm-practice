class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for (a, b), (c, d) in pairwise(points):
            ans += max(abs(a - c), abs(b - d))
        return ans