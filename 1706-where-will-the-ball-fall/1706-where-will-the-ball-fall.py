class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        ans = [0] * n
        for col in range(n):
            pos = col
            for row in range(m):
                if grid[row][pos] == 1:
                    if pos == n - 1 or grid[row][pos + 1] == -1:
                        pos = -1
                        break
                    else:
                        pos += 1
                else:
                    if pos == 0 or grid[row][pos - 1] == 1:
                        pos = -1
                        break
                    else:
                        pos -= 1
            ans[col] = pos
        return ans
                        