class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod = int(1e9+7)
        @cache
        def dp(n_, m_, k_):
            if n_ == 1:
                return k_ == 1
            ret = m_ * dp(n_ - 1, m_, k_)
            if k_ > 0:
                for i in range(1, m_):
                    ret += dp(n_ - 1, i, k_ - 1)
            # print(n_, m_, k_, ret)
            return ret % mod
        
        ans = 0
        for i in range(1, m + 1):
            ans += dp(n, i, k)
        return ans % mod