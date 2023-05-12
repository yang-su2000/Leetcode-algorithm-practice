class Solution:
    def mostPoints(self, qs: List[List[int]]) -> int:
        n = len(qs)
        dp = [-1] * n
        
        def rec(i):
            nonlocal n, dp
            if i >= n:
                return 0
            if dp[i] == -1:
                dp[i] = max(rec(i + 1), qs[i][0] + rec(i + 1 + qs[i][1]))
            return dp[i]
            
        return rec(0)