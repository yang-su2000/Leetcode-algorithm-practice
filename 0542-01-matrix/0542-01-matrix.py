class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        ans = [[inf] * m for _ in range(n)]
        cur = []
        for i in range(n):
            for j in range(m):
                if not mat[i][j]:
                    cur.append((i, j, 0))
                    ans[i][j] = 0
        d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while cur:
            nxt = []
            for i, j, dist in cur:
                if ans[i][j] < dist:
                    continue
                for di, dj in d:
                    i2, j2 = i + di, j + dj
                    if 0 <= i2 < n and 0 <= j2 < m and dist + 1 < ans[i2][j2]:
                        ans[i2][j2] = dist + 1
                        nxt.append((i2, j2, dist + 1))
            cur = nxt
        return ans