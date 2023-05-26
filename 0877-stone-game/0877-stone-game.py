class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def dp(l, r):
            if l == r:
                return piles[l]
            if piles[l] - dp(l+1, r) < piles[r] - dp(l, r-1):
                return piles[r] + dp(l, r-1)
            else:
                return piles[l] + dp(l+1, r)
        
        return dp(0, len(piles)-1)
            
            