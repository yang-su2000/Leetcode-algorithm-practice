class Solution:
    def new21Game(self, n: int, k: int, m: int) -> float:
        if k == 0:
            return 1.0
        nk = n - k + 1
        val = min(1.0, nk / m)
        if k == 1:
            return val
        dp = [1.0, val]
        dsum = [1.0, 1.0 + val]
        while nk < n:
            val = 1 / m * dsum[-1]
            if len(dsum) > m:
                val -= 1 / m * dsum[-m-1]
            plen = min(m, nk + 1)
            if len(dp) < plen:
                val += 1 / m * (plen - len(dp))
            dp.append(val)
            dsum.append(dsum[-1] + val)
            nk += 1
        # print(dp)
        return dp[-1]