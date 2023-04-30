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
            return 0
        if self.size[i] < self.size[j]:
            i, j = j, i
        self.parent[j] = i
        self.size[i] += self.size[j]
        return 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        U1 = Union(n)
        U2 = Union(n)
        e = 0
        for t, i, j in edges:
            i -= 1
            j -= 1
            if t == 3:
                e += min(1, U1.link(i, j) + U2.link(i, j))
        for t, i, j in edges:
            i -= 1
            j -= 1
            if t == 1:
                e += U1.link(i, j)
            elif t == 2:
                e += U2.link(i, j)
        if U1.size[U1.find(0)] != n:
            return -1
        if U2.size[U2.find(0)] != n:
            return -1
        return len(edges) - e