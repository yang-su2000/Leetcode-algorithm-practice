class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        t0, t1, t2 = 0, 1, 1
        while n > 2:
            t0, t1, t2 = t1, t2, t0 + t1 + t2
            n -= 1
        return t2