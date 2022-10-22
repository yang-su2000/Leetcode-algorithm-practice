class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        nls, mls = [], []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    nls.append(i)
                    mls.append(j)
        mls.sort()
        # print(nls, mls)
        if len(nls) % 2:
            ni = nls[len(nls)//2]
            mi = mls[len(mls)//2]
        else:
            ni = (nls[len(nls)//2-1] + nls[len(nls)//2]) // 2
            mi = (mls[len(mls)//2-1] + mls[len(mls)//2]) // 2
        # print(ni, mi)
        ans = sum([abs(ni - nls[k]) + abs(mi - mls[k]) for k in range(len(nls))])
        return ans