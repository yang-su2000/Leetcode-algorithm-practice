class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0] * n for _ in range(n)]
        ds = [(0,1), (1,0), (0,-1), (-1,0)]
        d = 0
        cur = 1
        i, j = 0, 0
        max = n * n
        while cur <= max:
            ans[i][j] = cur
            ni = i + ds[d][0]
            nj = j + ds[d][1]
            if 0 <= ni < n and 0 <= nj < n and ans[ni][nj] == 0:
                i, j = ni, nj
            else:
                d = (d + 1) % 4
                i, j = i + ds[d][0], j + ds[d][1]
            cur += 1
        return ans