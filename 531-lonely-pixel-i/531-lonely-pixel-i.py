class Solution:
    def findLonelyPixel(self, pic: List[List[str]]) -> int:
        m, n = len(pic), len(pic[0])
        rows, cols = [0] * m, [0] * n
        for i in range(m):
            for j in range(n):
                if pic[i][j] == 'B':
                    rows[i] += 1
                    cols[j] += 1
        ans = 0
        for i in range(m):
            for j in range(n):
                if pic[i][j] == 'B' and rows[i] == 1 and cols[j] == 1:
                    ans += 1
        return ans