class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        A = [[] for _ in range(n)]
        for i in range(n):
            x, y, r = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, r2 = bombs[j]
                if (x - x2) ** 2 + (y - y2) ** 2 <= r ** 2:
                    A[i].append(j)
        ans = 0
        
        def dfs(i, vis):
            nonlocal A
            ret = 1
            for j in A[i]:
                if not vis[j]:
                    vis[j] = True
                    ret += dfs(j, vis)
            return ret   
        
        for i in range(n):
            vis = [False] * n
            vis[i] = True
            ans = max(ans, dfs(i, vis))
                
        return ans