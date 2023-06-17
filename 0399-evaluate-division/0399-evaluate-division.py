class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        A = defaultdict(lambda: {})
        for (a, b), val in zip(equations, values):
            A[a][b] = val
            A[b][a] = 1. / val
        print(A)
        ans = []
        for a, b in queries:
            if a not in A or b not in A:
                ans.append(-1)
                continue
            cur = [(a, 1.)]
            d = {a: 1.}
            done = False
            while cur:
                node, val = cur.pop()
                if node == b:
                    ans.append(val)
                    done = True
                    break
                for child, val2 in A[node].items():
                    if child in d:
                        continue
                    cur.append((child, val * val2))
                    d[child] = val * val2
            # print(d.items())
            if not done:
                ans.append(-1)
        return ans