class Solution:
    def mostPoints(self, qs: List[List[int]]) -> int:
        @cache
        def rec(i):
            return max(rec(i + 1), qs[i][0] + rec(i + 1 + qs[i][1])) if i < len(qs) else 0
        return rec(0)