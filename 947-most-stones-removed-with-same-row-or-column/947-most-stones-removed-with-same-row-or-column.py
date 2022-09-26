class Union:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        
    def find(self, i):
        # root = i
        # while self.parent[root] != root:
        #     root = self.parent[root]
        # while i != root:
        #     parent_i = self.parent[i]
        #     self.parent[parent_i] = root
        #     i = parent_i
        # return root
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def connect(self, i, j):
        i, j = self.find(i), self.find(j)
        if i != j:
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
        # print(U.parent)
        for i in range(n):
            U.find(i)
        # print(U.parent)
        return n - len(set(U.parent))