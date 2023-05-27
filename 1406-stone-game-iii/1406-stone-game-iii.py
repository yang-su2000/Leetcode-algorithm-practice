class Solution:
    def stoneGameIII(self, ls: List[int]) -> str:
        n = len(ls)
        for i in range(n-2, -1, -1):
            ls[i] += ls[i+1]
        # print(ls)
        d = [None] * n

        def dp(i): # (val, # stones)
            nonlocal n, d
            if i >= n:
                return (0, 0)
            if d[i]:
                return d[i]
            val = inf
            stone = None
            for j in range(i+1, i+4):
                val2, _ = dp(j)
                if val2 < val:
                    val = val2
                    stone = j-i
            d[i] = (ls[i] - val, stone)
            return d[i]
        
        val, stone = dp(0)
        if stone < n:
            val -= d[stone][0]
        if val > 0:
            return 'Alice'
        elif val == 0:
            return 'Tie'
        else:
            return 'Bob'