class Solution:
    def countVowelPermutation(self, n: int) -> int:
        mod = int(1e9+7)
        dp = [[1] * 5 for _ in range(n)]
        # a / e / i / o / u
        # e, i, u -> a
        # a, i -> e
        # e, o -> i
        # i -> o
        # i, o -> u
        for i in range(1, n):
            dp[i][0] = (dp[i-1][1] + dp[i-1][2] + dp[i-1][4]) % mod
            dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % mod
            dp[i][2] = (dp[i-1][1] + dp[i-1][3]) % mod
            dp[i][3] = dp[i-1][2] % mod
            dp[i][4] = (dp[i-1][2] + dp[i-1][3]) % mod
        return sum(dp[n-1]) % mod