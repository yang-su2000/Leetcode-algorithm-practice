class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n = len(words)
        w = len(words[0])
        t = len(target)
        mod = int(1e9+7)
        d = [defaultdict(int) for _ in range(w)]
        for i in range(n):
            for j in range(w):
                c = words[i][j]
                d[j][c] += 1
        dp = [[0] * w for _ in range(t)]
        for j in range(w):
            dp[0][j] = d[j][target[0]]
        for i in range(1, t):
            psum = 0
            c = target[i]
            for j in range(w):
                dp[i][j] = (psum * d[j][c]) % mod
                psum += dp[i-1][j]
        return sum(dp[t-1]) % mod