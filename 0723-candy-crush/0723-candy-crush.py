class Solution:
    def erase_one(self, board, ret, i, j):
        if 1 <= i <= self.n - 2 and board[i-1][j] == board[i][j] == board[i+1][j] != 0:
            ret[i-1][j] = ret[i][j] = ret[i+1][j] = 0
            self.done = False
        if 1 <= j <= self.m - 2 and board[i][j-1] == board[i][j] == board[i][j+1] != 0:
            ret[i][j-1] = ret[i][j] = ret[i][j+1] = 0
            self.done = False
    
    def erase(self, board):
        ret = copy.deepcopy(board)
        for i in range(self.n):
            for j in range(self.m):
                self.erase_one(board, ret, i, j)
        return ret
    
    def drop(self, board):
        for j in range(self.m):
            i = self.n - 1
            i2 = self.n - 1
            while i >= 0:
                if board[i][j] > 0:
                    board[i2][j] = board[i][j]
                    i2 -= 1
                i -= 1
            while i2 >= 0:
                board[i2][j] = 0
                i2 -= 1
    
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        self.n, self.m = len(board), len(board[0])
        self.done = False
        while not self.done:
            self.done = True
            board = self.erase(board)
            self.drop(board)
        return board