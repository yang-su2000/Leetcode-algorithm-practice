class Solution:
    def climbStairs(self, n: int) -> int:
        x1 = 0
        x2 = 1
        for _ in range(n):
            x1, x2 = x2, x1 + x2
        return x2