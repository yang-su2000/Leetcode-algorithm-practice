class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        A = [[] for _ in range(n)]
        for x, y, w in roads:
            x -= 1
            y -= 1
            A[x].append((y, w))
            A[y].append((x, w))
        
        def dij(start):
            ans = [inf] * n
            ans[start] = appleCost[start]
            cur = [(appleCost[start], start)]
            while cur:
                cost, node = heappop(cur)
                if cost > ans[node]:
                    continue
                for child, w in A[node]:
                    cost2 = cost - appleCost[node] + appleCost[child] + w * (k + 1)
                    if cost2 < ans[child]:
                        ans[child] = cost2
                        heappush(cur, (cost2, child))
            return min(ans)
        
        ret = [0] * n
        for i in range(n):
            ret[i] = dij(i)
        return ret