class Solution:
    def checkStraightLine(self, ls: List[List[int]]) -> bool:
        dy = ls[1][1] - ls[0][1]
        dx = ls[1][0] - ls[0][0]
        n = len(ls)
        for i in range(1, n - 1):
            x1, y1 = ls[i]
            x2, y2 = ls[i+1]
            if (y2 - y1) * dx != (x2 - x1) * dy:
                return False
        return True