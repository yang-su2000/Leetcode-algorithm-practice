class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        pre = [[0] * n for _ in range(n)]
        for x1, y1, x2, y2 in queries:
            for i in range(x1, x2+1):
                pre[i][y1] += 1
                if y2 < n - 1:
                    pre[i][y2+1] -= 1
        ans = [[0] * n for _ in range(n)]
        for i in range(n):
            ans[i][0] = pre[i][0]
        for i in range(n):
            for j in range(1, n):
                ans[i][j] = ans[i][j-1] + pre[i][j]
        return ans