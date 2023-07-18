class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = abs(x), abs(y)
        if x < y:
            x, y = y, x
        if x == 1 and y == 0:
            return 3
        if x == 2 and y == 2:
            return 4
        diff = x - y
        if diff < y:
            return diff - (diff - y) // 3 * 2
        return diff - (diff - y) // 4 * 2