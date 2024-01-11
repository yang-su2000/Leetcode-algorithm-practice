class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        if a == e:
            x, y = min(b, f), max(b, f)
            if not (x < d < y and c == a):
                return 1
        if b == f:
            x, y = min(a, e), max(a, e)
            if not (x < c < y and d == b):
                return 1
        def sign(x):
            return 1 if x > 0 else -1
        if abs(e - c) == abs(f - d):
            dx = sign(e - c)
            dy = sign(f - d)
            flag = True
            for x, y in zip(range(c, e, dx), range(d, f, dy)):
                if (x, y) == (a, b):
                    flag = False
                    break
            if flag:
                return 1
        return 2