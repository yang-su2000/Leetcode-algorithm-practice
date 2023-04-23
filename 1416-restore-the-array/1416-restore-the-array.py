class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        m = len(str(k))
        mod = int(1e9+7)
        dp = [0] * n
        for i in range(n):
            for j in range(i - m + 1, i + 1):
                if j >= 0 and s[j] != '0' and 1 <= int(s[j: i+1]) <= k:
                    dp[i] += (dp[j-1] if j > 0 else 1)
            dp[i] %= mod
        # print(dp)
        return dp[-1]