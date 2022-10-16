class Solution:
    def minDifficulty(self, ls: List[int], d: int) -> int:
        if len(ls) < d:
            return -1
        dp_ = [[None] * d for _ in range(len(ls))]
        cmax = 0
        for i in range(len(ls)-1, -1, -1):
            cmax = max(cmax, ls[i])
            dp_[i][0] = cmax
        
        # what is the min diff given [c] cuts and last cut before index [i]
        def dp(i, c):
            if dp_[i][c] is not None:
                return dp_[i][c]
            cmax = 0
            ans = float('inf')
            for j in range(i+1, len(ls)):
                cmax = max(cmax, ls[j-1])
                ans = min(ans, cmax + dp(j, c-1))
            dp_[i][c] = ans
            return ans
        
        return dp(0, d-1)