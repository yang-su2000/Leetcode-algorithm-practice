class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m = len(grid)
        n = len(grid[0])
        cur = []
        vis = set()
        keys = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    cur.append((0, i, j))
                    vis.add((0, i, j))
                elif 'a' <= grid[i][j] <= 'f':
                    keys |= (1 << (ord(grid[i][j]) - ord('a')))
        print(keys)
        d = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        ans = 0
        while cur:
            nxt = []
            for state, i, j in cur:
                # print(ans, state, i, j)
                if state == keys:
                    return ans
                for di, dj in d:
                    i2, j2 = i + di, j + dj
                    if 0 <= i2 < m and 0 <= j2 < n and grid[i2][j2] != '#':
                        state2 = state
                        if 'a' <= grid[i2][j2] <= 'f':
                            state2 |= (1 << (ord(grid[i2][j2]) - ord('a')))
                        elif 'A' <= grid[i2][j2] <= 'F':
                            if not (state2 & (1 << (ord(grid[i2][j2]) - ord('A')))):
                                continue
                        s = (state2, i2, j2)
                        if s not in vis:
                            nxt.append(s)
                            vis.add(s)
            cur = nxt
            ans += 1
        return -1