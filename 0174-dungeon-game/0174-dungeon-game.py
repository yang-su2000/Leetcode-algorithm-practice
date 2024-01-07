class Solution:
    def calculateMinimumHP(self, d: List[List[int]]) -> int:
        n, m = len(d), len(d[0])  
        dp = [[inf] * m for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                nex = min(dp[i+1][j] if i < n-1 else inf, dp[i][j+1] if j < m-1 else inf)
                if nex == inf:
                    dp[i][j] = 1 - min(0, d[i][j])
                else:
                    dp[i][j] = max(1, nex - d[i][j])
        # print(dp)
        return dp[0][0]