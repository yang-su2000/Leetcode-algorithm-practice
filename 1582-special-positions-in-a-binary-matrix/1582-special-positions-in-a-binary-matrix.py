class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rsum = [0] * m
        csum = [0] * n
        for i in range(m):
            rsum[i] = sum(mat[i])
        for j in range(n):
            for i in range(m):
                csum[j] += mat[i][j]
        ans = 0
        for i in range(m):
            for j in range(n):
                if rsum[i] == csum[j] == 1 and mat[i][j]:
                    ans += 1
        return ans