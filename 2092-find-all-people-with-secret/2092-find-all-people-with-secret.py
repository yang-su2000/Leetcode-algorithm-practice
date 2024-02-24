class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        limit = max(t for _, _, t in meetings)
        ls = [[] for _ in range(limit + 1)]
        for x, y, t in meetings:
            ls[t].append((x, y))
        ans = [False] * n
        ans[0] = ans[firstPerson] = True
        for t in range(1, limit + 1):
            d = defaultdict(list)
            cur = set()
            for x, y in ls[t]:
                if ans[x] and ans[y]:
                    continue
                if ans[x]:
                    cur.add(x)
                if ans[y]:
                    cur.add(y)
                d[x].append(y)
                d[y].append(x)
            cur = list(cur)
            while cur:
                node = cur.pop()
                for child in d[node]:
                    if ans[child]:
                        continue
                    ans[child] = True
                    cur.append(child)
        return [i for i in range(n) if ans[i]]