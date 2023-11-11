class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.A = [[] for _ in range(n)] # (to, val)
        for a, b, cost in edges:
            self.A[a].append((b, cost))

    def addEdge(self, edge: List[int]) -> None:
        a, b, cost = edge
        self.A[a].append((b, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        if node1 == node2:
            return 0
        d = [inf] * self.n
        cur = [(0, node1)]
        d[node1] = 0
        while cur:
            val, a = heapq.heappop(cur)
            for b, cost in self.A[a]:
                d2 = d[a] + cost
                if d2 < d[b]:
                    d[b] = d2
                    heapq.heappush(cur, (d2, b))
        return d[node2] if d[node2] < inf else -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)