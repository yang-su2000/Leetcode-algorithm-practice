class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)] # [left, right]
        for i in range(n):
            dp[i][i] = 1
        for l in range(2, n+1):
            for i in range(n-l+1):
                dp[i][i+l-1] = max(dp[i][i+l-2], dp[i+1][i+l-1], (2 + dp[i+1][i+l-2] if s[i] == s[i+l-1] else 0))
        # print(dp)
        return dp[0][n-1]
        