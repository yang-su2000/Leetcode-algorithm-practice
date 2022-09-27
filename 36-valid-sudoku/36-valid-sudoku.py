class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isRow(board) and self.isCol(board) and self.isCell(board)
    
    def isRow(self, board):
        for row in board:
            d = Counter(row)
            for digit, count in d.items():
                if digit != '.' and count > 1:
                    return False
        return True
    
    def isCol(self, board):
        for i in range(9):
            d = Counter()
            for j in range(9):
                d[board[j][i]] += 1
            for digit, count in d.items():
                if digit != '.' and count > 1:
                    return False
        return True
    
    def isCell(self, board):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                d = Counter()
                for m in range(3):
                    for n in range(3):
                        d[board[i+m][j+n]] += 1
                for digit, count in d.items():
                    if digit != '.' and count > 1:
                        return False
        return True