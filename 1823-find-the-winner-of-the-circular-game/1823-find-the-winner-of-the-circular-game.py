class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        d = [i for i in range(1, n + 1)]
        i = 0
        while len(d) > 1:
            i = (i + k - 1) % len(d)
            d.pop(i)
            i %= len(d)
        return d[0]