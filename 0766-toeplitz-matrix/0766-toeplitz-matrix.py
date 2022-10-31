class Solution:
    def isToeplitzMatrix(self, mat: List[List[int]]) -> bool:
        m, n = len(mat), len(mat[0])
        for row in range(m):
            cur = None
            for diag in range(max(m, n)):
                i = row + diag
                j = diag
                if 0 <= i < m and 0 <= j < n:
                    if cur is None:
                        cur = mat[i][j]
                    elif cur != mat[i][j]:
                        return False
        for col in range(n):
            cur = None
            for diag in range(max(m, n)):
                i = diag
                j = col + diag
                if 0 <= i < m and 0 <= j < n:
                    if cur is None:
                        cur = mat[i][j]
                    elif cur != mat[i][j]:
                        return False
        return True