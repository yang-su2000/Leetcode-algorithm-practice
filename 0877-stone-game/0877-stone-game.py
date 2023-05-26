class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def dp(l, r): # my stone - # opponent stone
            if l == r:
                return piles[l]
            return max(piles[l] - dp(l+1, r), piles[r] - dp(l, r-1))
        
        return dp(0, len(piles)-1) > 0
            