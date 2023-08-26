class Solution:
    def uniquePathsWithObstacles(self, g: List[List[int]]) -> int:
        m = len(g)
        n = len(g[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1 if g[0][0] == 0 else 0
        for i in range(1, m):
            if g[i][0] == 0:
                dp[i][0] = dp[i-1][0]
        for j in range(1, n):
            if g[0][j] == 0:
                dp[0][j] = dp[0][j-1]
        for i in range(1, m):
            for j in range(1, n):
                if g[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # print(dp)
        return dp[-1][-1]