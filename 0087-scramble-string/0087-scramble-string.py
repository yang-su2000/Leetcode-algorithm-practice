class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)
        dp = [[[False] * n for _ in range(n)] for L in range(n)] # dp[l][i][j]
        for i in range(n):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[0][i][j] = True
        for L in range(2, n+1):
            for i in range(n-L+1):
                for j in range(n-L+1):
                    for l in range(1, L):
                        l2 = L - l
                        # print(L, i, j, l)
                        if (dp[l-1][i][j] and dp[l2-1][i+l][j+l]):
                            # print(L, i, j, L, 'v')
                            dp[L-1][i][j] = True
                            break
                        if (dp[l-1][i][j+l2] and dp[l2-1][i+l][j]):
                            # print(L, i, j, L, '^')
                            dp[L-1][i][j] = True
                            break
        return dp[n-1][0][0]