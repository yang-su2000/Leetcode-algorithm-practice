class Solution:
    def countRoutes(self, ls: List[int], a: int, b: int, f: int) -> int:
        @cache
        def dp(a_, f_): return sum(a_ == b if a_ == b_ else dp(b_, f_ - abs(ls[a_] - ls[b_])) for b_ in range(len(ls))) % 1000000007 if f_ >= 0 else 0
        return dp(a, f)