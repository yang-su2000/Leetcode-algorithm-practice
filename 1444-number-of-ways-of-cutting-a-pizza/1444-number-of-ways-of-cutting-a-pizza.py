class Solution:  
    def ways(self, pizza: List[str], k: int) -> int:
        if k == 1:
            return 1
        n = len(pizza)
        m = len(pizza[0])
        psum = [[0] * m for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                psum[i][j] = (1 if pizza[i][j] == 'A' else 0)
                if i != n-1:
                    psum[i][j] += psum[i+1][j]
                if j != m-1:
                    psum[i][j] += psum[i][j+1]
                if i != n-1 and j != m-1:
                    psum[i][j] -= psum[i+1][j+1]
        # print(psum)
        dp = [[0] * m for _ in range(n)]
        mod = int(1e9+7)
        for i in range(n-1, 0, -1):
            sum1 = psum[0][0]
            sum2 = psum[i][0]
            if sum2 and sum1 - sum2:
                dp[i][0] = 1
        for j in range(m-1, 0, -1):
            sum1 = psum[0][0]
            sum2 = psum[0][j]
            if sum2 and sum1 - sum2:
                dp[0][j] = 1
        # print(dp)
        for _ in range(k-2):
            dp2 = [[0] * m for _ in range(n)]
            for i in range(n):
                for j in range(m):
                    if dp[i][j] == 0:
                        continue
                    for i2 in range(n-1, i, -1):
                        sum1 = psum[i][j]
                        sum2 = psum[i2][j]
                        if sum2 and sum1 - sum2:
                            dp2[i2][j] = (dp2[i2][j] + dp[i][j]) % mod
                    for j2 in range(m-1, j, -1):
                        sum1 = psum[i][j]
                        sum2 = psum[i][j2]
                        if sum2 and sum1 - sum2:
                            dp2[i][j2] = (dp2[i][j2] + dp[i][j]) % mod
            dp = dp2
            # print(dp)
        return sum([sum(row) for row in dp]) % mod