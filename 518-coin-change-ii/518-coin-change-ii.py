class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = 1
        for i in range(n):
            for j in range(1, amount + 1):
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j - coins[i] >= 0:
                    dp[i][j] += dp[i][j-coins[i]]
        # print(dp)
        return dp[n-1][amount]
