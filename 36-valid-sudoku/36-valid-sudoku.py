class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        cells = [0] * 9
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                val = 1 << (int(board[i][j]) - 1)
                if rows[i] & val:
                    return False
                rows[i] |= val
                if cols[j] & val:
                    return False
                cols[j] |= val
                cell_i = i // 3 * 3 + j // 3
                if cells[cell_i] & val:
                    return False
                cells[cell_i] |= val
        return True