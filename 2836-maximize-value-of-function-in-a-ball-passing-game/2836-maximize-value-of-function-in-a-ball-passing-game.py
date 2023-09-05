class Solution:
    def getMaxFunctionValue(self, childs: List[int], k: int) -> int:
        n = len(childs)
        # res[start pos] = (end pos, val) at k steps
        res = [(i, i) for i in range(n)]
        # dp[start pos] = (end pos, val) at each 2^i steps
        dp = [(childs[p], childs[p]) for p in range(n)]
        for i in range(40):
            if k & (1 << i):
                for cur_pos in range(n):
                    start_pos, val = res[cur_pos]
                    end_pos, val2 = dp[start_pos]
                    res[cur_pos] = (end_pos, val + val2)
            dp2 = [None] * n
            for start_pos in range(n):
                mid_pos, val = dp[start_pos]
                end_pos, val2 = dp[mid_pos]
                dp2[start_pos] = (end_pos, val + val2)
            dp = dp2
        return max(val for pos, val in res)
    
    
    
    