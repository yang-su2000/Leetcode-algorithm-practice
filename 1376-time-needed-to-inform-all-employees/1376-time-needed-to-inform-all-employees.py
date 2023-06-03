class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        A = [[] for _ in range(n)]
        head = None
        for i in range(n):
            if manager[i] != -1:
                A[manager[i]].append(i)
            else:
                head = i
        
        def dfs(i):
            return (max([dfs(j) for j in A[i]]) if A[i] else 0) + informTime[i]
        
        return dfs(head)
            