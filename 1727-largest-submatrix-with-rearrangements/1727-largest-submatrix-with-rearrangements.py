class Solution:
    def largestSubmatrix(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        ans = 0
        for row in range(m):
            for col in range(n):
                if mat[row][col] and row:
                    mat[row][col] += mat[row-1][col]
            cur = sorted(mat[row])
            for col in range(n):
                ans = max(ans, cur[col] * (n - col))
        return ans