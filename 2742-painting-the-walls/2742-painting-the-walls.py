class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        d = defaultdict(lambda: inf)
        d[-1] = 0
        d[time[0]] = cost[0]
        n = len(cost)
        for i in range(1, n):
            t, c = time[i], cost[i]
            d2 = defaultdict(lambda: inf)
            for t2, c2 in d.items():
                d2[t2-1] = min(d2[t2-1], c2)
                d2[t2+t] = min(d2[t2+t], c + c2)
            # d2[-1] = min(d2[-1], 0)
            # d2[t] = min(d2[t], c)
            d = d2
            # print(d)
        ans = inf
        for t, c in d.items():
            if t >= 0:
                ans = min(ans, c)
        return ans