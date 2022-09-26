class Union:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def connect(self, i, j):
        i, j = self.find(i), self.find(j)
        self.parent[i] = j

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        U = Union(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    U.connect(i, j)
        for i in range(n):
            U.find(i)
        return len(set(U.parent))