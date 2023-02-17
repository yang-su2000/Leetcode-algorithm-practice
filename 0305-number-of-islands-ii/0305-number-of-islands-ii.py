class Union:
    def __init__(self):
        self.d = {}
        self.ds = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
    def add(self, i, j):
        self.d[(i, j)] = (i, j)
        
    def find(self, i, j):
        i2, j2 = self.d[(i, j)]
        if i != i2 or j != j2:
            self.d[(i, j)] = self.find(i2, j2)
            return self.d[(i, j)]
        else:
            return i, j
    
    def link_count(self, i, j):
        ps = set()
        for di, dj in self.ds:
            i2, j2 = i + di, j + dj
            if (i2, j2) in self.d:
                ps.add(self.find(i2, j2))
        for i2, j2 in ps:
            self.d[(i2, j2)] = (i, j)
        return len(ps)

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        U = Union()
        ans = []
        counts = 0
        for i, j in positions:
            if (i, j) in U.d:
                ans.append(counts)
                continue
            U.add(i, j)
            count = U.link_count(i, j)
            counts = counts + 1 - count
            ans.append(counts)
        return ans