class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        a, b, c = costs[0]
        for i in range(1, len(costs)):
            a2, b2, c2 = costs[i]
            a, b, c = min(b, c) + a2, min(a, c) + b2, min(a, b) + c2
        return min(a, b, c)
        