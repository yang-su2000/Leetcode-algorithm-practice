class Solution:
    def countRoutes(self, ls: List[int], start: int, end: int, fuel: int) -> int:
        mod = 10 ** 9 + 7
        
        @cache
        def dp(x, f):
            return sum(x == end if z == x else dp(z, f - abs(ls[x] - ls[z])) for z in range(len(ls))) % mod if f >= 0 else 0
        
        return dp(start, fuel)