class Union:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def link(self, i, j):
        i = self.find(i)
        j = self.find(j)
        if i == j:
            return
        if self.size[i] < self.size[j]:
            i, j = j, i
        self.parent[j] = i
        self.size[i] += self.size[j]

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        U = Union(n)
        queries = sorted([(d, u, v, i) for i, (u, v, d) in enumerate(queries)])
        edgeList = sorted(edgeList, key=lambda x: x[2])
        ans = [None] * len(queries)
        ei = 0
        for d, u, v, i in queries:
            while ei < len(edgeList) and edgeList[ei][2] < d:
                U.link(edgeList[ei][0], edgeList[ei][1])
                ei += 1
            ans[i] = (U.find(u) == U.find(v))
        return ans