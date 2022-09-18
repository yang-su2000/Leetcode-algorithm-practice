class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        routes = [set(route) for route in routes] # turn each bus index into a set
        G = defaultdict(set) # the node is the bus index
        for i, r1 in enumerate(routes):
            for j in range(i+1, len(routes)):
                r2 = routes[j]
                if r1 & r2: # check if set intersection non-empty
                    G[i].add(j)
                    G[j].add(i)
        # print(G.items())
        seen, targets = set(), set()
        for node, route in enumerate(routes):
            if source in route:
                seen.add(node)
            if target in route:
                targets.add(node)
        cur = [(node, 1) for node in seen]
        for i, dist in cur:
            if i in targets:
                return dist
            for j in G[i]:
                if j not in seen:
                    seen.add(j)
                    cur.append((j, dist + 1))
        return -1
    