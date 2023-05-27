class Solution:
    def stoneGameIII(self, ls: List[int]) -> str:
        n = len(ls)
        d = [None] * n
        
        def dp(i): # my stone - # opponent stone
            nonlocal n, d
            if i >= n:
                return 0
            if d[i]:
                return d[i]
            d[i] = max(ls[i] - dp(i+1), sum(ls[i:i+2]) - dp(i+2), sum(ls[i:i+3]) - dp(i+3))
            return d[i]
        
        ans = dp(0)
        if ans > 0:
            return 'Alice'
        elif ans == 0:
            return 'Tie'
        else:
            return 'Bob'