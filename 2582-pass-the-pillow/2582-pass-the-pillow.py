class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        re = time % (2 * n - 2)
        if re > n - 1:
            return n - (re - (n - 1))
        return 1 + re