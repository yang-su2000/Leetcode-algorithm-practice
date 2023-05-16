class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = len(costs[0])
        dp = [[0] * k for _ in range(n)]
        dp[0] = costs[0]
        for i in range(1, n):
            for k1 in range(k): # cur
                cur = inf
                for k2 in range(k): # prev
                    if k1 == k2:
                        continue
                    cur = min(cur, dp[i-1][k2])
                dp[i][k1] = cur + costs[i][k1]
        # print(dp)
        return min(dp[-1])