import heapq

class Solution:
    def minimumCost(self, start: List[int], target: List[int], roads: List[List[int]]) -> int:
        start = tuple(start)
        target = tuple(target)
        nodes = set([start, target])
        A = defaultdict(lambda: defaultdict(lambda: inf)) # a -> b -> dist
        for a1, a2, b1, b2, d in roads:
            a = (a1, a2)
            b = (b1, b2)
            nodes.add(a)
            nodes.add(b)
            A[a][b] = min(A[a][b], d)
        for a in nodes:
            for b in nodes:
                if a == b:
                    continue
                A[a][b] = min(A[a][b], abs(a[1] - b[1]) + abs(a[0] - b[0]))
        # print(nodes)
        # print(A)
        ds = defaultdict(lambda: inf)
        ds[start] = 0
        pq = [(0, start)]
        while pq:
            d, a = heappop(pq)
            if d > ds[a]:
                continue
            if a == target:
                # print(ds)
                # print(pq)
                return d
            for b, d2 in A[a].items():
                if d + d2 < ds[b]:
                    ds[b] = d + d2
                    heappush(pq, (d + d2, b))