class Solution:
    def rootCount(self, edges: List[List[int]], guesses: List[List[int]], k: int) -> int:
        n = len(edges) + 1
        A = [[] for _ in range(n)]
        g = [set() for _ in range(n)]
        for a, b in edges:
            A[a].append(b)
            A[b].append(a)
        for u, v in guesses:
            g[u].add(v)
        
        # dfs on index 0
        def dfs(node, parent):
            nonlocal p
            for child in A[node]:
                if child == parent:
                    continue
                if child in g[node]:
                    p += 1
                dfs(child, node)
        
        # rerooting
        def dfs2(node, parent, p):
            nonlocal ans
            for child in A[node]:
                if child == parent:
                    continue
                p2 = p
                if child in g[node] and node in g[child]:
                    pass
                elif child in g[node]:
                    p2 -= 1
                elif node in g[child]:
                    p2 += 1
                if p2 >= k:
                    ans += 1
                dfs2(child, node, p2)
        
        p = 0
        dfs(0, -1)
        ans = (1 if p >= k else 0)
        dfs2(0, -1, p)
        return ans