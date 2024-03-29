class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        dp[0] = 1
        c = set([s[0]])
        mod = int(1e9+7)
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                dp[i] += dp[j]
                if s[j] == s[i]:
                    break
            if s[i] not in c:
                c.add(s[i])
                dp[i] += 1
            dp[i] %= mod
        # print(dp)
        return sum(dp) % mod