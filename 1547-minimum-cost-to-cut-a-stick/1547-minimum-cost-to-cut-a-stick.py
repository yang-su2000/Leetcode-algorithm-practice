class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.extend([0, n])
        cuts.sort()
        m = len(cuts)
        dp = [[inf] * m for _ in range(m)] # idx l to r
        for i in range(m-1):
            dp[i][i+1] = 0
        for i in range(m-2):
            dp[i][i+2] = cuts[i+2] - cuts[i]
        for l in range(3, m):
            for i in range(m-l):
                # print(l, i)
                dp[i][i+l] = cuts[i+l] - cuts[i]
                dp[i][i+l] += min([dp[i][i+j] + dp[i+j][i+l] for j in range(l)])
        # print(dp)
        return dp[0][m-1]