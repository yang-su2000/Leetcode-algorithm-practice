class Solution:
    def countRoutes(self, ls: List[int], start: int, end: int, fuel: int) -> int:
        mod = 10 ** 9 + 7
        
        @cache
        def dp(x, f):
            if f < 0:
                return 0
            ret = (x == end)
            for z in range(len(ls)):
                if z == x:
                    continue
                if abs(ls[x] - ls[z]) <= f:
                    ret += dp(z, f - abs(ls[x] - ls[z]))
            # print(x, f, ret)
            return ret % mod
        
        return dp(start, fuel)