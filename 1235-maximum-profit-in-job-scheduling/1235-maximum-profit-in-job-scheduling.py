class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1]) # sort by endtime
        dp = [[0, 0]] # (end, max_profit)
        for start, end, profit in jobs:
            # only compare first value (prev_end), get prev_end <= start
            i = bisect.bisect(dp, [start + 1]) - 1
            # current max = current + prev_max
            profit += dp[i][1]
            # only add if we get more profit
            # caz otherwise prev_end <= end with prev_profit >= profit is better for future
            if profit > dp[-1][1]:
                dp.append([end, profit])
        return dp[-1][1]