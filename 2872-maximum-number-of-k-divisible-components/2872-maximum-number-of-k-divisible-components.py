class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        A = [[] for _ in range(n)]
        for a, b in edges:
            A[a].append(b)
            A[b].append(a)
        ans = 0

        def dfs(node, parent):
            nonlocal ans, A
            ret = values[node]
            for child in A[node]:
                if child == parent:
                    continue
                ret += dfs(child, node)
            if ret % k == 0:
                ans += 1
                ret = 0
            return ret
        
        dfs(0, -1)
        return ans
        
        