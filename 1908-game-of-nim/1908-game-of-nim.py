class Solution:
    def nimGame(self, piles: List[int]) -> bool:
        base = tuple([0] * len(piles))
        
        @cache
        def dp(cur):
            nonlocal base
            if cur == base:
                return False
            ls = list(cur)
            for i in range(len(ls)):
                c = ls[i]
                for j in range(1, c + 1):
                    ls[i] -= j
                    if not dp(tuple(ls)):
                        return True
                    ls[i] += j
            return False
            
        return dp(tuple(piles))