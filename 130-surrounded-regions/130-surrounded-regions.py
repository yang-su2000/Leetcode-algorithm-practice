class Union:
    def __init__(self):
        self.parents = {}
        self.flips = {}
        
    def find(self, i):
        if self.parents[i] != i:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]
    
    def union(self, i, j):
        if not i in self.parents or not j in self.parents:
            return
        i, j = self.find(i), self.find(j)
        self.parents[i] = j
        self.flips[j] = (self.flips[i] and self.flips[j])

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        U = Union()
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    continue
                U.parents[(i,j)] = (i,j)
                U.flips[(i,j)] = (0 < i < m-1 and 0 < j < n-1)
                U.union((i,j), (i-1,j))
                U.union((i,j), (i,j-1))
                U.union((i,j), (i+1,j))
                U.union((i,j), (i,j+1))
        for i, j in U.parents.keys():
            if U.flips[U.find((i, j))]:
                board[i][j] = 'X'
                