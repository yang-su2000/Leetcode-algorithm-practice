class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        ans = 0
        n = len(edges) + 1
        A = [[] for _ in range(n)]
        for a, b in edges:
            A[a].append(b)
            A[b].append(a)
        
        def dfs(node, parent):
            nonlocal ans
            cur = []
            for child in A[node]:
                if child == parent:
                    continue
                cur.append(dfs(child, node) + 1)
            if not cur:
                return 0
            cur.sort()
            if len(cur) >= 2:
                ans = max(ans, cur[-1] + cur[-2])
            else:
                ans = max(ans, cur[-1])
            return cur[-1]
        
        dfs(0, -1)
        return ans