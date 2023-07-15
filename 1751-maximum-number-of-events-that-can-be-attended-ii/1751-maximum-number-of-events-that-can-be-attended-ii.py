from bisect import bisect_right

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])
        ends = [end for _, end, _ in events]
        n = len(events)
        dp = [[0] * (k + 1) for _ in range(n)]
        for i in range(n):
            a, b, val = events[i]
            pi = bisect_left(ends, a) - 1
            for j in range(k, 0, -1):
                not_pick = dp[i-1][j] if i else 0
                pick = val + (dp[pi][j-1] if pi >= 0 else 0)
                dp[i][j] = max(not_pick, pick)
                # print(i, j, pi, not_pick, pick)
        # print(dp)
        return dp[-1][-1]