class Solution:
    def numWays(self, n: int, k: int) -> int:
        a, a2 = k, 0
        for _ in range(n - 1):
            a, a2 = (k - 1) * (a + a2), a
        return a + a2