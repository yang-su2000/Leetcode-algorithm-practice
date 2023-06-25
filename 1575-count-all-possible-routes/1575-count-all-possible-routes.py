class Solution:
    def countRoutes(self, ls: List[int], start: int, end: int, fuel: int) -> int:
        @cache
        def dp(a, f): return sum(a == end if a == b else dp(b, f - abs(ls[a] - ls[b])) for b in range(len(ls))) % 1000000007 if f >= 0 else 0
        return dp(start, fuel)