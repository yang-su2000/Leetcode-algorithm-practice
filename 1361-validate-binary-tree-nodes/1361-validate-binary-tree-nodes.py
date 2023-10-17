class Solution:
    def validateBinaryTreeNodes(self, n: int, l: List[int], r: List[int]) -> bool:
        vis = [False] * n
        parent = [False] * n
        for a, b in zip(l, r):
            if a != -1:
                parent[a] = True
            if b != -1:
                parent[b] = True
        cur = []
        for i in range(n):
            if not parent[i]:
                cur.append(i)
                vis[i] = True
                break
        if not cur:
            return False
        count = 1
        while cur:
            node = cur.pop()
            if l[node] != -1:
                if vis[l[node]]:
                    return False
                vis[l[node]] = True
                count += 1
                cur.append(l[node])
            if r[node] != -1:
                if vis[r[node]]:
                    return False
                vis[r[node]] = True
                count += 1
                cur.append(r[node])
        return count == n