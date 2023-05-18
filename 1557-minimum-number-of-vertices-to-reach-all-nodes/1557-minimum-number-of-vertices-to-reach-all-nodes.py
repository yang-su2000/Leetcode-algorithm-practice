class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        vis = [False] * n
        for a, b in edges:
            vis[b] = True
        ans = []
        for i in range(n):
            if not vis[i]:
                ans.append(i)
        return ans