class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n, m = len(ring), len(key)
        d = [min(i, n-i) for i in range(n)]
        for c in key:
            d2 = [inf] * n
            for i in range(n):
                if d[i] == inf:
                    continue
                for j in range(n):
                    if ring[j] != c:
                        continue
                    diff = abs(j - i)
                    d2[j] = min(d2[j], d[i] + 1 + min(diff, n - diff))
            d = d2
            # print(d)
        ans = inf
        for i in range(n):
            if ring[i] == key[-1]:
                ans = min(ans, d[i])
        return ans