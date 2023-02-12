class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        d = {}
        for l in range(1, 31):
            for i in range(len(s) - l + 1):
                s2 = s[i:i+l]
                if s2 not in d:
                    d[s2] = i
        # print(d.items())
        n = len(queries)
        ans = [None] * n
        for i in range(n):
            q1, q2 = queries[i]
            target = str(bin(q1 ^ q2))[2:]
            if target in d:
                idx = d[target]
                ans[i] = [idx, idx + len(target) - 1]
            else:
                ans[i] = [-1, -1]
        return ans