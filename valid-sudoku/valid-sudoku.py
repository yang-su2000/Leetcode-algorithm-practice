class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def valid(row):
            for key, val in Counter(row).items():
                if key != '.' and val > 1:
                    return False
            return True
        
        # row
        for row in board:
            if not valid(row):
                return False
    
        # col
        for j in range(9):
            ls = []
            for i in range(9):
                num = board[i][j]
                ls.append(num)
            if not valid(ls):
                return False
    
        # each big cell
        for I in range(3):
            for J in range(3):
                ls = []
                # each small cell
                for i in range(3):
                    i += 3 * I
                    for j in range(3):
                        j += 3 * J
                        num = board[i][j]
                        ls.append(num)
                if not valid(ls):
                    return False
        
        return True
        