class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        n = len(prob)
        dp = [[0] * (target + 1) for _ in range(n)]
        base = 1
        for c in range(n):
            base *= (1 - prob[c])
            dp[c][0] = base
        if target == 0:
            return dp[-1][0]
        dp[0][1] = prob[0]
        for c in range(1, n):
            for t in range(1, target + 1):
                dp[c][t] = dp[c-1][t] * (1 - prob[c]) + dp[c-1][t-1] * prob[c]
        # print(dp)
        return dp[-1][-1]
                