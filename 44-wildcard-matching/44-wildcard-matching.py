class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sn, pn = len(s), len(p)
        dp = [[0] * (sn + 1) for _ in range(pn + 1)] # before (pi, si) all cleared
        dp[0][0] = 1
        for pi in range(pn + 1):
            for si in range(sn + 1):
                if not dp[pi][si]:
                    continue
                if dp[pi][si] == 2 and si < sn:
                    dp[pi][si+1] = 2
                if not pi < pn:
                    continue
                if p[pi] == '*':
                    dp[pi+1][si] = 2
                elif si < sn and (p[pi] == '?' or p[pi] == s[si]):
                    dp[pi+1][si+1] = max(1, dp[pi+1][si+1])
        return dp[-1][-1]
        