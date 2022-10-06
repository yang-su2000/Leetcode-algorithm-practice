class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        ans = 0
        for i in range(n):
            d = {13141516: 1}
            for j in range(i+1, n):
                # if points[j][0] == points[i][0] and points[j][1] == points[i][1]:
                #     exit(1)
                slope = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0]) \
                    if points[j][0] != points[i][0] else 13141516
                if slope not in d:
                    d[slope] = 1
                d[slope] += 1
            ans = max(ans, max(d.values()))
        return ans