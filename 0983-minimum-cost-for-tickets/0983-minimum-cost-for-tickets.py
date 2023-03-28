class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * 366
        flag = [False] * 366
        for d in days:
            flag[d] = True
        for d in range(1, 366):
            if not flag[d]:
                dp[d] = dp[d-1]
            else:
                dp[d] = costs[0] + dp[d-1]
                dp[d] = min(dp[d], costs[1] + (dp[d-7] if d >= 7 else 0))
                dp[d] = min(dp[d], costs[2] + (dp[d-30] if d >= 30 else 0))
        # print(dp[:21])
        return dp[365]