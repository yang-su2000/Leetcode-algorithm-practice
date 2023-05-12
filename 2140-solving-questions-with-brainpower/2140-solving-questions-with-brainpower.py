class Solution:
    def mostPoints(self, qs: List[List[int]]) -> int:
        n = len(qs)
        dp = [-1] * n
        
        @cache
        def rec(i):
            nonlocal n, dp
            return max(rec(i + 1), qs[i][0] + rec(i + 1 + qs[i][1])) if i < n else 0
            
        return rec(0)