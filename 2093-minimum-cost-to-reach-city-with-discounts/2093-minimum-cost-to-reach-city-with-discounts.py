class Solution:
    def minimumCost(self, n: int, highways: List[List[int]], discounts: int) -> int:
        costs = [[inf] * n for _ in range(discounts + 1)]
        costs[discounts][0] = 0
        A = [[] for _ in range(n)]
        for a, b, cost in highways:
            A[a].append((b, cost))
            A[b].append((a, cost))
        pq = [(0, discounts, 0)] # [cost, discount, node]
        while pq:
            cost, discount, node = heappop(pq)
            if cost > costs[discount][node]:
                continue
            for child, cost2 in A[node]:
                # not use discount
                if cost + cost2 < costs[discount][child]:
                    costs[discount][child] = cost + cost2
                    heappush(pq, (cost + cost2, discount, child))
                # use discount
                if 1 <= discount and cost + cost2 // 2 < costs[discount-1][child]:
                    costs[discount-1][child] = cost + cost2 // 2
                    heappush(pq, (cost + cost2 // 2, discount - 1, child))
        ans = min(costs[i][n-1] for i in range(discounts + 1))
        # print(costs)
        if ans == inf:
            ans = -1
        return ans