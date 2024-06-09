class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        islands = []
        
        def dfs(x, y):
            island = []
            d = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            cur = [(x, y)]
            while cur:
                x, y = cur.pop()
                island.append((x, y))
                for dx, dy in d:
                    x2, y2 = x + dx, y + dy
                    if 0 <= x2 < m and 0 <= y2 < n and grid[x2][y2] == 1:
                        cur.append((x2, y2))
                        grid[x2][y2] = 0
            return island
        
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 0:
                    continue
                grid[x][y] = 0
                island = dfs(x, y)
                islands.append(island)
        
        # print(islands)
        k = len(islands)
        ans = 0
        for i in range(k):
            distinct = True
            for j in range(i + 1, k):
                island = islands[i]
                target = islands[j]
                if len(island) != len(target):
                    continue
                diff = (target[0][0] - island[0][0], target[0][1] - island[0][1])
                same = True
                # print(i, j, island, target)
                for (x, y), (x2, y2) in zip(island, target):
                    if (x2 - x) != diff[0] or (y2 - y) != diff[1]:
                        same = False
                        break
                if same:
                    distinct = False
                    break
            if distinct:
                ans += 1
        return ans