class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        ls = sorted(zip(ages, scores)) # (age, score) increasing
        ls = [score for _, score in ls]
        n = len(ls)
        # print(ls)
        dp = [0] * n
        for i in range(n):
            dp[i] = ls[i]
            for j in range(i):
                if ls[j] <= ls[i]:
                    dp[i] = max(dp[i], dp[j] + ls[i])
        # print(dp)
        return max(dp)