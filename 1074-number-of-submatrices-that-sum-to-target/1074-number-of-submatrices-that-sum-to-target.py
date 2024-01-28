class Solution:
    def numSubmatrixSumTarget(self, pmat: List[List[int]], target: int) -> int:
        m, n = len(pmat), len(pmat[0])
        for i in range(m):
            for j in range(n):
                if i > 0: pmat[i][j] += pmat[i-1][j]
                if j > 0: pmat[i][j] += pmat[i][j-1]
                if i > 0 and j > 0: pmat[i][j] -= pmat[i-1][j-1]
            # print(pmat[i])
        ans = 0
        for l in range(n):
            for r in range(l, n):
                d = defaultdict(int)
                d[target] = 1
                for i in range(m - 1, -1, -1):
                    cur = pmat[m-1][r]
                    if l > 0: cur -= pmat[m-1][l-1]
                    if i > 0: cur -= pmat[i-1][r]
                    if l > 0 and i > 0: cur += pmat[i-1][l-1]
                    # print(i, l, r, cur, targets[l][r][cur])
                    ans += d[cur]
                    d[cur + target] += 1
        return ans