class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        for i in range(n-1):
            piles[i+1] += piles[i]
        
        @cache
        def dp(l, r):
            ret = piles[r]
            if l > 0:
                ret -= piles[l-1]
            if l == r:
                return ret
            ret -= min(dp(l+1, r), dp(l, r-1))
            return ret
        
        return dp(0, n-1)
            
            