class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, k = len(s1), len(s2), len(s3)
        d = set([(0, 0)]) # (s1 idx, s2 idx)
        for i in range(k):
            d2 = set()
            for x, y in d:
                if x < n and s1[x] == s3[i]:
                    d2.add((x + 1, y))
                if y < m and s2[y] == s3[i]:
                    d2.add((x, y + 1))
            d = d2
            # print(d)
            if not d:
                return False
        return (n, m) in d