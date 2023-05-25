class Solution:
    def new21Game(self, n: int, k: int, m: int) -> float:
        if k == 0:
            return 1.0
        nk = n - k + 1
        val = min(1.0, nk / m)
        if k == 1:
            return val
        dp = [1.0, 1.0 + val]
        while nk < n:
            val = dp[-1]
            if len(dp) > m:
                val -= dp[-m-1]
            val += max(0, min(m, nk + 1) - len(dp))
            dp.append(val * 1 / m + dp[-1])
            nk += 1
        # print(dp)
        return val * 1 / m