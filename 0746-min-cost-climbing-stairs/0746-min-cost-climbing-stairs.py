class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        v1, v2 = 0, 0
        for i in range(2, n + 1):
            v1, v2 = min(v1 + cost[i-1], v2 + cost[i-2]), v1
        return v1