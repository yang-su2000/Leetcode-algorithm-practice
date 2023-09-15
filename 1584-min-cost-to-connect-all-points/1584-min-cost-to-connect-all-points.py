class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        cur = [(0, 0)]
        vis = [False] * len(points)
        ans = 0
        while cur:
            dist, i = heappop(cur)
            if vis[i]:
                continue
            ans += dist
            vis[i] = True
            for j, child in enumerate(points):
                if vis[j]:
                    continue
                dist2 = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heappush(cur, (dist2, j))
        return ans