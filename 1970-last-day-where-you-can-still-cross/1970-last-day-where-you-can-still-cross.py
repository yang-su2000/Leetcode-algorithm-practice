class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        state = [[0] * col for _ in range(row)]
        for i, (a, b) in enumerate(cells):
            state[a-1][b-1] = i + 1
        l, r = 0, row * col
        d = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        def solve(day):
            nonlocal state, d
            cur = []
            vis = set()
            for j in range(col):
                if state[0][j] > day:
                    if 0 == row - 1:
                        return True
                    cur.append((0, j))
                    vis.add((0, j))
            while cur:
                nxt = []
                for i, j in cur:
                    for di, dj in d:
                        i2, j2 = i + di, j + dj
                        if 0 <= i2 < row and 0 <= j2 < col and state[i2][j2] > day and (i2, j2) not in vis:
                            if i2 == row - 1:
                                return True
                            nxt.append((i2, j2))
                            vis.add((i2, j2))
                cur = nxt
            return False
        
        while l < r:
            mid = (l + r) // 2 + 1
            if solve(mid):
                l = mid
            else:
                r = mid - 1
        return l