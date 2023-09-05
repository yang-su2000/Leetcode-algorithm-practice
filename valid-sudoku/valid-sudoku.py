class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # row
        for row in board:
            for key, val in Counter(row).items():
                if key != '.' and val > 1:
                    return False
    
        # col
        for j in range(9):
            c = Counter()
            for i in range(9):
                num = board[i][j]
                if num == '.':
                    continue
                if c[num] == 1:
                    print(2)
                    return False
                c[num] += 1
    
        # each sub cell
        for I in range(3):
            for J in range(3):
                c = Counter()
                for i in range(I * 3, I * 3 + 3):
                    for j in range(J * 3, J * 3 + 3):
                        num = board[i][j]
                        if num == '.':
                            continue
                        if c[num] == 1:
                            print(3)
                            return False
                        c[num] += 1
        
        return True
        