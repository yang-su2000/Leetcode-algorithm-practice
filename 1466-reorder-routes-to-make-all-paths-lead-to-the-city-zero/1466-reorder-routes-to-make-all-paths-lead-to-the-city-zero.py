class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        ins = [[] for _ in range(n)]
        outs = [[] for _ in range(n)]
        for a, b in connections:
            ins[b].append(a)
            outs[a].append(b)
        ans = 0
        
        def dfs(cur, parent):
            nonlocal ans
            for child in outs[cur]:
                if child == parent:
                    continue
                ans += 1
                dfs(child, cur)
            for child in ins[cur]:
                if child == parent:
                    continue
                dfs(child, cur)
        
        dfs(0, -1)
        return ans