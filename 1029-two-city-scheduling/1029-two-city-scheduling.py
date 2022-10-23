class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        d = defaultdict(lambda: float('inf'))
        d[(0, 0)] = 0
        for c0, c1 in costs:
            d2 = defaultdict(lambda: float('inf'))
            d2[(0, 0)] = 0
            for (p0, p1), cost in d.items():
                if p0 < n:
                    d2[(p0 + 1, p1)] = min(d2[(p0 + 1, p1)], cost + c0)
                if p1 < n:
                    d2[(p0, p1 + 1)] = min(d2[(p0, p1 + 1)], cost + c1)
            d = d2
            # print(d.items())
        return d[(n, n)]