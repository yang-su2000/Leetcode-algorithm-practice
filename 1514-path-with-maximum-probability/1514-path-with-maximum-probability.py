from heapq import *

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], p: List[float], start: int, end: int) -> float:
        A = [[] for _ in range(n)]
        for (a, b), val in zip(edges, p):
            A[a].append((b, val))
            A[b].append((a, val))
        d = [0.] * n
        d[start] = 1.
        cur = [(-1., start)]
        while cur:
            val, node = heappop(cur)
            val = -val
            if d[node] > val:
                continue
            if node == end:
                return val
            for child, val2 in A[node]:
                if val * val2 > d[child]:
                    d[child] = val * val2
                    heappush(cur, (-d[child], child))
        return 0.