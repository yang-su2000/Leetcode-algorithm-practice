class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(1, len(s) + 1):
            if 1 <= i and '1' <= s[i-1] <= '9':
                dp[i] += dp[i-1]
            if 2 <= i and (s[i-2] == '1' or (s[i-2] == '2' and s[i-1] <= '6')):
                dp[i] += dp[i-2]
        return dp[-1]