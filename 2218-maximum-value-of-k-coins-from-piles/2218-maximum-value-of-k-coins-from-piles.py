class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        n = len(piles)
        dp = [[0] * (k+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, k+1):
                psum = 0
                for j2 in range(min(len(piles[i-1]), j) + 1):
                    psum += piles[i-1][j2-1] if j2 else 0
                    dp[i][j] = max(dp[i][j], dp[i-1][j-j2] + psum)
        return dp[n][k]