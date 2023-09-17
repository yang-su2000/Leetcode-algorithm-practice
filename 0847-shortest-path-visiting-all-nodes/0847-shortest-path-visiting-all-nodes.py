class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        d = [[inf] * n for _ in range(n)]
        for node, childs in enumerate(graph):
            for child in childs:
                d[node][child] = 1
        for i in range(n):
            d[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])
        @cache
        def dp(node, bit):
            if bit == (1 << n) - 1:
                return 0
            ret = inf
            for child in range(n):
                if bit & (1 << child) == 0:
                    ret = min(ret, d[node][child] + dp(child, bit | (1 << child)))
            return ret
        return min(dp(node, (1 << node)) for node in range(n))