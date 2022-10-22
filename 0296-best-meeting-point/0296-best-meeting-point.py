class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        nls, mls = [], []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    nls.append(i)
        for j in range(m):
            for i in range(n):
                if grid[i][j] == 1:
                    mls.append(j)
        # print(nls, mls)
        ni = nls[len(nls)//2]
        mi = mls[len(mls)//2]
        # print(ni, mi)
        ans = sum([abs(ni - nls[k]) + abs(mi - mls[k]) for k in range(len(nls))])
        return ans