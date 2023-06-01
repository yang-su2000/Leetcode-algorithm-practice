class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        n = len(prob)
        dp = [[0] * (target + 2) for _ in range(n)]
        dp[0][0] = 1 - prob[0]
        dp[0][1] = prob[0]
        for c in range(1, n):
            for t in range(target + 1):
                dp[c][t] = dp[c-1][t] * (1 - prob[c]) + (dp[c-1][t-1] if t else 0) * prob[c]
        # print(dp)
        return dp[n-1][target]
                