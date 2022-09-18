class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        n = max([stop for route in routes for stop in route]) + 1
        edges = [[] for _ in range(n)]
        visits = [False] * n
        for i, route in enumerate(routes):
            for node in route:
                edges[node].append(i)
        if source >= n or target >= n or not edges[target]:
            return -1
        curs = [source]
        visits[source] = True
        dist = 0
        while curs:
            nxts = []
            for node in curs:
                if node == target:
                    return dist
                for bus_idx in edges[node]: # take bus_idx
                    for node2 in routes[bus_idx]:
                        if visits[node2]:
                            continue
                        nxts.append(node2)
                        visits[node2] = True
            dist += 1
            curs = nxts
        return -1
    