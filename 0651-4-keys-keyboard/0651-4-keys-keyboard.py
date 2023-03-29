class Solution:
    def maxA(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            mval = dp[i-1] + 1
            for j in range(3, i):
                mval = max(mval, dp[i-j] * (j - 1))
            dp[i] = mval
        return dp[n]