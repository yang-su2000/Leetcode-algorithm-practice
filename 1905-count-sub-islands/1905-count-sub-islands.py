class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        def dfs(grid, dirs=[(1, 0), (0, 1), (-1, 0), (0, -1)]):
            # return G = modified grid, A = [(island id) -> grid idxs]
            n, m = len(grid), len(grid[0])
            G = [[-1] * m for _ in range(n)]
            A = []
            for i in range(n):
                for j in range(m):
                    if G[i][j] != -1 or grid[i][j] == 0:
                        continue
                    gid = len(A)
                    G[i][j] = gid
                    a = []
                    cur = [(i, j)]
                    while cur:
                        a.append(cur[-1])
                        x, y = cur.pop()
                        for dx, dy in dirs:
                            x2, y2 = x + dx, y + dy
                            if 0 <= x2 < n and 0 <= y2 < m and grid[x2][y2] == 1 and G[x2][y2] == -1:
                                G[x2][y2] = gid
                                cur.append((x2, y2))
                    A.append(a)
            return G, A
        
        G1, A1 = dfs(grid1)
        G2, A2 = dfs(grid2)
        # print(G1)
        # print(A1)
        # print(G2)
        # print(A2)
        ans = 0
        for a in A2:
            s = set()
            valid = True
            for x, y in a:
                s.add(G1[x][y])
                if len(s) > 1 or G1[x][y] == -1:
                    valid = False
                    break
            ans += valid
        return ans