class Solution:
    def largestSubmatrix(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        ans = 0
        f = [0] * n
        for row in range(m):
            f2 = [0] * n
            for col in range(n):
                if f[col]:
                    f2[col] = f[col] - 1
                else:
                    for row2 in range(row, m):
                        if mat[row2][col] == 0:
                            break
                        f2[col] += 1
            f = f2
            cur = sorted(f)
            for col in range(n):
                ans = max(ans, cur[col] * (n - col))
        return ans