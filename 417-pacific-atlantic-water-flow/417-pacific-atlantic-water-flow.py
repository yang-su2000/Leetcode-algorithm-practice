class Solution:
    def pacificAtlantic(self, h: List[List[int]]) -> List[List[int]]:
        m, n = len(h), len(h[0])
        po = [[False] * n for _ in range(m)]
        ao = [[False] * n for _ in range(m)]
        pls = []
        als = []
        for i in range(m):
            po[i][0] = True
            pls.append((i, 0))
            ao[i][n-1] = True
            als.append((i, n-1))
        for j in range(n):
            po[0][j] = True
            pls.append((0, j))
            ao[m-1][j] = True
            als.append((m-1, j))
        d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        while pls:
            i, j = pls.pop()
            for di, dj in d:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and \
                not po[ni][nj] and h[ni][nj] >= h[i][j]:
                    po[ni][nj] = True
                    pls.append((ni, nj))
        while als:
            i, j = als.pop()
            for di, dj in d:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and \
                not ao[ni][nj] and h[ni][nj] >= h[i][j]:
                    ao[ni][nj] = True
                    als.append((ni, nj))
        # print(po)
        # print(ao)
        ans = []
        for i in range(m):
            for j in range(n):
                if ao[i][j] and po[i][j]:
                    ans.append([i,j])
        return ans
    