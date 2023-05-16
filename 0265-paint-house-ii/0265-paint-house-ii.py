class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = len(costs[0])
        pq = [[] for _ in range(n)] # (min_cost, idx)
        for i in range(n):
            for j in range(k):
                if i and j == pq[i-1][1][1]:
                    prev = -pq[i-1][0][0]
                elif i:
                    prev = -pq[i-1][1][0]
                else:
                    prev = 0
                cur = costs[i][j] + prev
                heapq.heappush(pq[i], (-cur, j))
                if len(pq[i]) > 2:
                    heapq.heappop(pq[i])
        # print(pq)
        return min(-pq[-1][0][0], -pq[-1][1][0])