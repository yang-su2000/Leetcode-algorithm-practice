class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def solve(effort):
            cur = [(0, 0)]
            r, h = len(heights), len(heights[0])
            vis = [[False] * h for _ in range(r)]
            vis[0][0] = True
            d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
            while cur:
                i, j = cur.pop()
                for di, dj in d:
                    i2, j2 = i + di, j + dj
                    if 0 <= i2 < r and 0 <= j2 < h and not vis[i2][j2]:
                        if abs(heights[i2][j2] - heights[i][j]) <= effort:
                            vis[i2][j2] = True
                            cur.append((i2, j2))
            return vis[-1][-1]
        
        l, r = 0, int(1e6)
        while l < r:
            mid = (l + r) // 2
            if solve(mid):
                r = mid
            else:
                l = mid + 1
        return l
            