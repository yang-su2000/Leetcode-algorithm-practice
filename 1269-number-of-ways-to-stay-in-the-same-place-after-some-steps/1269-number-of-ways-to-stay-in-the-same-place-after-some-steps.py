class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        mod = int(1e9+7)
        dp = defaultdict(int)
        dp[0] = 1
        for _ in range(steps):
            dp2 = defaultdict(int)
            for pos, count in dp.items():
                for i in range(-1, 2):
                    if 0 <= pos + i < arrLen:
                        dp2[pos + i] = (dp2[pos + i] + count) % mod
            dp = dp2
        return dp[0]