class Union:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1] * size
        
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def connect(self, i, j):
        i, j = self.find(i), self.find(j)
        if self.size[i] > self.size[j]:
            self.size[i] += self.size[j]
            self.parent[j] = i
        else:
            self.size[j] += self.size[i]
            self.parent[i] = j

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        U = Union(n)
        for i in range(n):
            si = stones[i]
            for j in range(n):
                sj = stones[j]
                if si[0] == sj[0] or si[1] == sj[1]:
                    U.connect(i, j)
        for i in range(n):
            U.find(i)
        return n - len(set(U.parent))