class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[0] * (target + 1) for _ in range(n)]
        for ki in range(1, k + 1):
            if ki <= target:
                dp[0][ki] = 1
        modulo = 10**9 + 7
        for i in range(1, n):
            for j in range(1, target + 1):
                for ki in range(1, k + 1):
                    if 0 <= j-ki:
                        dp[i][j] += dp[i-1][j-ki]
                dp[i][j] %= modulo
        # print(dp)
        return dp[-1][-1]