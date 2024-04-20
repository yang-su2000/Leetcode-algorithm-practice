class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(land)
        m = len(land[0])
        for i in range(n):
            for j in range(m):
                if land[i][j] == 0:
                    continue
                lx, rx = i, i
                ly, ry = j, j
                for rx in range(i, n):
                    if land[rx][j] == 0:
                        rx = rx - 1
                        break
                for ry in range(j, m):
                    if land[i][ry] == 0:
                        ry = ry - 1
                        break
                ans.append([lx, ly, rx, ry])
                for x in range(lx, rx + 1):
                    for y in range(ly, ry + 1):
                        land[x][y] = 0
        return ans