class Union:
    def __init__(self, n):
        self.ls = [i for i in range(n)]
        
    def find(self, i):
        if self.ls[i] != i:
            self.ls[i] = self.find(self.ls[i])
        return self.ls[i]
    
    def connect(self, i, j):
        i = self.find(i)
        j = self.find(j)
        self.ls[i] = j

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        U = Union(n)
        for i in range(n):
            s = strs[i]
            for j in range(i+1, n):
                s2 = strs[j]
                p = None
                switch = False
                for k in range(m):
                    s2 = strs[j]
                    if s[k] != s2[k]:
                        if switch:
                            p = -1
                            break
                        if p is None:
                            p = (s[k], s2[k])
                        elif s[k] == p[1] and s2[k] == p[0]:
                            p = None
                            switch = True
                        else:
                            p = -1
                            break
                if p is None:
                    U.connect(i, j)
        return len(set([U.find(i) for i in range(n)]))