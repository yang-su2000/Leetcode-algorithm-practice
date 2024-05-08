class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        A = [[] for _ in range(n)]
        for x, y, w in roads:
            x -= 1
            y -= 1
            A[x].append((y, w))
            A[y].append((x, w))

        ans = appleCost.copy()
        cur = [(appleCost[i], i) for i in range(n)]
        heapify(cur)
        while cur:
            cost, node = heappop(cur)
            if cost > ans[node]:
                continue
            for child, w in A[node]:
                cost2 = cost + w * (k + 1)
                if cost2 < ans[child]:
                    ans[child] = cost2
                    heappush(cur, (cost2, child))
        return ans