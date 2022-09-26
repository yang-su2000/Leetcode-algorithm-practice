class Union:
    def __init__(self, size):
        self.ls = [i for i in range(size)]
        
    def find(self, i):
        if self.ls[i] != i:
            self.ls[i] = self.find(self.ls[i])
        return self.ls[i]
    
    def isconnect(self, i, j):
        return self.find(i) == self.find(j)
    
    def connect(self, i, j):
        i, j = self.find(i), self.find(j)
        if i != j:
            self.ls[i] = j

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        U = Union(27)
        ls = [False] * 27
        dis = []
        for e in equations:
            c1, c2 = ord(e[0]) - ord('a'), ord(e[-1]) - ord('a')
            eq = True if e[1] == '=' else False
            if eq:
                U.connect(c1, c2)
            else:
                dis.append((c1, c2))
        for c1, c2 in dis:
            if U.isconnect(c1, c2):
                return False
        return True