class Union:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.rank = [1] * n
        
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def link(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.p[y] = x
        self.rank[x] += self.rank[y]

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def MST(edges):
            U = Union(n)
            ret = 0
            for a, b, w in edges:
                if U.find(a) != U.find(b):
                    U.link(a, b)
                    ret += abs(w)
            # print(ret, edges)
            return ret
        
        min_weight = MST(sorted(edges, key=lambda x: x[2]))
        # print(min_weight)
        cri, pcri = [], []
        for i in range(len(edges)):
            w = edges[i][2]
            edges[i][2] = inf
            cri_weight = MST(sorted(edges, key=lambda x: x[2]))
            if cri_weight > min_weight:
                cri.append(i)
            else:
                edges[i][2] = -w
                pcri_weight = MST(sorted(edges, key=lambda x: x[2]))
                if pcri_weight == min_weight:
                    pcri.append(i)
            edges[i][2] = w
        return [cri, pcri]