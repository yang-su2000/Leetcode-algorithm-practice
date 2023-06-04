class Solution:
    def dfs(self, i, n, M):
        self.visited[i] = 1
        for j in range(n):
            if not self.visited[j] and M[i][j]:
                self.dfs(j, n, M)
    
    def findCircleNum(self, M: List[List[int]]) -> int:
        n = len(M)
        self.visited = [0] * n
        ans = 0
        for i in range(n):
            if not self.visited[i]:
                ans += 1
                self.dfs(i, n, M)
        return ans