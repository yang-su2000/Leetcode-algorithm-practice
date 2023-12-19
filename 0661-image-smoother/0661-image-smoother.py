class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        n, m = len(img), len(img[0])
        ans = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                i1, i2 = max(0, i - 1), min(n - 1, i + 1)
                j1, j2 = max(0, j - 1), min(m - 1, j + 1)
                for i_ in range(i1, i2 + 1):
                    for j_ in range(j1, j2 + 1):
                        ans[i][j] += img[i_][j_]
                ans[i][j] //= ((i2 - i1 + 1) * (j2 - j1 + 1))
        return ans