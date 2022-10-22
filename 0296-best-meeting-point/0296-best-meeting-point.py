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
            ni = [nls[len(nls)//2]]
            mi = [mls[len(mls)//2]]
        else:
            nval = nls[len(nls)//2-1] + nls[len(nls)//2]
            mval = mls[len(mls)//2-1] + mls[len(mls)//2]
            ni = [nval//2, nval//2+1] if nval % 2 else [nval//2]
            mi = [mval//2, mval//2+1] if mval % 2 else [mval//2]
        # print(ni, mi)
        ans = float('inf')
        for i in ni:
            for j in mi:
                ans = min(ans, sum([abs(i - nls[k]) + abs(j - mls[k]) for k in range(len(nls))]))
        return ans