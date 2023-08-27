class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        n = len(stones)
        dp = [set() for _ in range(n)]
        dp[1].add(1)
        d = {stones[i]: i for i in range(n)}
        for i in range(1, n):
            for k in dp[i]:
                for k2 in k - 1, k, k + 1:
                    p = stones[i] + k2
                    if p in d and d[p] > i:
                        dp[d[p]].add(k2)
        # print(dp)
        return dp[-1]