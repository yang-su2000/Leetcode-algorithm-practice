class Solution:
    def canFinish(self, n: int, pres: List[List[int]]) -> bool:
        childs = [[] for _ in range(n)]
        count = [0] * n
        for a, b in pres:
            count[a] += 1
            childs[b].append(a)
        ans = 0
        cur = []
        for i in range(n):
            if not count[i]:
                cur.append(i)
                ans += 1
        while cur:
            node = cur.pop()
            for child in childs[node]:
                count[child] -= 1
                if not count[child]:
                    cur.append(child)
                    ans += 1
        return ans == n