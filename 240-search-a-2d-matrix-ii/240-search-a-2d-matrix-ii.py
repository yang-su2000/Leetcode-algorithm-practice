class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        row = len(mat)
        col = len(mat[0])
        i = row - 1
        j = 0
        while i >= 0 and j < col:
            val = mat[i][j]
            if val > target:
                i -= 1
            elif val < target:
                j += 1
            else:
                return True
        return False