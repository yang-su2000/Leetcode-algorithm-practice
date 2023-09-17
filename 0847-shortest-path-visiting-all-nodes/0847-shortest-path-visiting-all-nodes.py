class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        t = (1 << n) - 1
        cache = {}
        def dp(node, bit):
            nonlocal n, t, cache
            state = (node, bit)
            if state in cache:
                return cache[state]
            if bit == (1 << node):
                return 0
            cache[state] = inf
            ret = inf
            for child in graph[node]:
                if bit & (1 << child):
                    ret = min(ret, 1 + dp(child, bit), 1 + dp(child, bit ^ (1 << node)))
            cache[state] = ret
            return ret
        
        return min(dp(node, (1 << n) - 1) for node in range(n))