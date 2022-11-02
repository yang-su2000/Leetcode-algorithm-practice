class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        ps = [True for i in range(2, n)]
        i = 0
        while i < min(len(ps), int(sqrt(n) + 1)):
            if ps[i]:
                p = i+2
                for p2 in range(p*p, n, p):
                    ps[p2-2] = False
            i += 1
        return sum(ps)
            