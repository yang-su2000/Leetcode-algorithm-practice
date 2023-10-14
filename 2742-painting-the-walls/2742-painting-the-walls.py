class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        @cache
        def dp(i, remain):
            # print(i, remain)
            if i == len(cost):
                return 0 if remain >= 0 else inf
            ret = inf
            if remain >= -len(cost):
                ret = min(ret, dp(i + 1, remain - 1))
            if remain <= len(cost):
                ret = min(ret, cost[i] + dp(i + 1, remain + time[i]))
            return ret
        return dp(0, 0)