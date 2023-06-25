class Solution:
    def countRoutes(self, ls: List[int], a: int, b: int, f: int) -> int:
        @cache
        def dp(a_, f_): return sum(a_ == b if a_ == i else dp(i, f_ - abs(ls[a_] - ls[i])) for i in range(len(ls))) % 1000000007 if f_ >= 0 else 0
        return dp(a, f)