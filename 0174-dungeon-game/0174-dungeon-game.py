class Solution:
    def calculateMinimumHP(self, d: List[List[int]]) -> int:
        n, m = len(d), len(d[0])
        
        def solve(val):
            dp = [[-inf] * m for _ in range(n)]
            dp[0][0] = val + d[0][0]
            for i in range(n):
                for j in range(m):
                    if i > 0 and dp[i-1][j] > 0:
                        dp[i][j] = max(dp[i][j], dp[i-1][j] + d[i][j])
                    if j > 0 and dp[i][j-1] > 0:
                        dp[i][j] = max(dp[i][j], dp[i][j-1] + d[i][j])
            # print(dp)
            return dp[-1][-1] > 0
        
        l = 1
        r = 399 * 1000 + 1
        while l < r:
            mid = (l + r) // 2
            if solve(mid):
                r = mid
            else:
                l = mid + 1
            # print(mid)
        return l