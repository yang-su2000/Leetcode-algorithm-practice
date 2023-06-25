class Solution:
    def countRoutes(self, ls: List[int], start: int, end: int, fuel: int) -> int:
        n = len(ls)
        mod = 10 ** 9 + 7
        
        @cache
        def dp(x, f):
            nonlocal ls, n, mod
            if f == 0:
                return 0
            if abs(ls[x] - ls[end]) > f:
                return 0
            ret = (x != end)
            for z in range(n):
                if z == x:
                    continue
                if abs(ls[x] - ls[z]) <= f:
                    ret = (ret + dp(z, f - abs(ls[x] - ls[z]))) % mod
            # print(x, f, ret)
            return ret % mod
        
        return dp(start, fuel) + (start == end)