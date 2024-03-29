class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        p = [0] * n
        p[0] = dp[0] = 1
        d = {s[0]: 0}
        mod = int(1e9+7)
        for i in range(1, n):
            c = s[i]
            dp[i] = p[i-1]
            if c in d and d[c]:
                dp[i] -= p[d[c] - 1]
            elif c not in d:
                dp[i] += 1
            d[c] = i
            p[i] = p[i-1] + dp[i]
        # print(dp, p)
        return sum(dp) % mod
