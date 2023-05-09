class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        USED_FLAG = 101
        ans = []
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i = 0
        x, y = 0, 0
        m, n = len(matrix), len(matrix[0])
        count = m * n
        while count > 0:
            ans.append(matrix[x][y])
            matrix[x][y] = USED_FLAG
            count -= 1
            x2, y2 = x + d[i][0], y + d[i][1]
            if 0 <= x2 and x2 < m and 0 <= y2 and y2 < n and matrix[x2][y2] != USED_FLAG:
                x, y = x2, y2
            else:
                i += 1
                if i == len(d):
                    i = 0
                x, y = x + d[i][0], y + d[i][1]
        return ans