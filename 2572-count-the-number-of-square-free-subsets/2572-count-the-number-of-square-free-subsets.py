class Solution:
    def __init__(self):
        s = set([4, 8, 9, 12, 16, 18, 20, 24, 25, 27, 28])
        d = defaultdict(set)
        for i in range(2, 31):
            if i in s:
                continue
            i2 = i
            f = 2
            while f <= i2:
                flag = False
                if i2 % f == 0:
                    i2 //= f
                    d[i].add(f)
                f += 1
        # print(d.items())
        primes = []
        for k, v in d.items():
            if len(v) == 1:
                primes.append(k)
        self.d = defaultdict(int)
        for k, v in d.items():
            b = 0
            for i in range(len(primes)):
                if primes[i] in v:
                    b |= (1 << i)
            self.d[k] = b
        self.d[1] = 0
        # print(self.d.items())
    
    def squareFreeSubsets(self, nums: List[int]) -> int:
        ls = []
        for i in nums:
            if i in self.d:
                ls.append(self.d[i])
        # print(ls)
        d = defaultdict(int)
        mod = int(1e9+7)
        for i in ls:
            d2 = defaultdict(int)
            for b, count in d.items():
                d2[b] = (d2[b] + count) % mod
                if (i & b) == 0:
                    d2[i | b] = (d2[i | b] + count) % mod
            d2[i] += 1
            d = d2
            # print(d.items())
        return sum(d.values()) % mod