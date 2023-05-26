class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        for i in range(n-2, -1, -1):
            piles[i] += piles[i+1]
        dp = [[0] * n for _ in range(n)]
        
        def solve(i, m):
            nonlocal n, dp
            # print(i, m)
            if i + 2*m >= n:
                return piles[i]
            if dp[i][m]:
                return dp[i][m]
            dp[i][m] = piles[i] - min([solve(i+x, max(m, x)) for x in range(1, 2*m+1)])
            return dp[i][m]
        
        return solve(0, 1)