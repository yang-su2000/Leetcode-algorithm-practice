class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        costs.sort(key=lambda c: c[0] - c[1])
        c0 = sum(c[0] for c in costs[:n])
        c1 = sum(c[1] for c in costs[n:])
        return c0 + c1