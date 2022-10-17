class Solution:
    def nthUglyNumber(self, n: int) -> int:
        fs = [2, 3, 5]
        vs = [0, 0, 0]
        ls = [1]
        for _ in range(n-1):
            cur = float('inf')
            idx = None
            for i in range(len(fs)):
                val = fs[i] * ls[vs[i]]
                if val < cur:
                    cur = val
                    idx = [i]
                elif val == cur:
                    idx.append(i)
            for i in idx:
                vs[i] += 1
            ls.append(cur)
        return ls[-1]