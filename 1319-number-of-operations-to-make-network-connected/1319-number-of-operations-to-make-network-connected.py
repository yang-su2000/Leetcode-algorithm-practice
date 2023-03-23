class Solution:
    def makeConnected(self, n: int, ls: List[List[int]]) -> int:
        m = len(ls)
        if m + 1 < n:
            return -1
        A = [[] for _ in range(n)]
        for a, b in ls:
            A[a].append(b)
            A[b].append(a)
        ans = 0
        vis = [0] * n
        
        def dfs(node):
            nonlocal vis
            for child in A[node]:
                if not vis[child]:
                    vis[child] = ans
                    dfs(child)
        
        for node in range(n):
            if not vis[node]:
                ans += 1
                vis[node] = ans
                dfs(node)
            
        return ans - 1