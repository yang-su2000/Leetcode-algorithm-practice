class Solution:
    def getMaxFunctionValue(self, childs: List[int], k: int) -> int:
        n = len(childs)
        res = [(i, i) for i in range(n)] # final (pos, val)
        dp = [(childs[i], childs[i]) for i in range(n)] # 2^i (pos, val)
        for i in range(40):
            if k & (1 << i):
                for i in range(n):
                    pos, val = res[i]
                    pos2, val2 = dp[pos]
                    res[i] = (pos2, val + val2)
            dp2 = [None] * n
            for i in range(n):
                pos, val = dp[i]
                pos2, val2 = dp[pos]
                dp2[i] = (pos2, val + val2)
            dp = dp2
        return max(val for pos, val in res)