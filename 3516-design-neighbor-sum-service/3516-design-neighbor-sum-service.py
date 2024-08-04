class neighborSum:

    def __init__(self, grid: List[List[int]]):
        n = len(grid)
        self.n = n
        self.idxs = [None] * (n * n)
        self.grid = grid
        for i in range(n):
            for j in range(n):
                val = grid[i][j]
                self.idxs[val] = (i, j)

    def getVal(self, i, j):
        if 0 <= i < self.n and 0 <= j < self.n:
            return self.grid[i][j]
        else:
            return 0 

    def adjacentSum(self, value: int) -> int:
        i, j = self.idxs[value]
        return self.getVal(i-1, j) + self.getVal(i, j-1) + self.getVal(i+1, j) + self.getVal(i, j+1)

    def diagonalSum(self, value: int) -> int:
        i, j = self.idxs[value]
        return self.getVal(i-1, j-1) + self.getVal(i-1, j+1) + self.getVal(i+1, j-1) + self.getVal(i+1, j+1)
        


# Your neighborSum object will be instantiated and called as such:
# obj = neighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)