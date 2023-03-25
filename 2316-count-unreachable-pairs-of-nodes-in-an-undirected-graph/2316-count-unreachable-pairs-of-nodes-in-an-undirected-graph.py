class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        A = [[] for _ in range(n)]
        for a, b in edges:
            A[a].append(b)
            A[b].append(a)
        group = 0
        labels = [-1] * n
        
        def dfs(node, group):
            nonlocal A, labels
            cur = [node]
            while cur:
                node = cur.pop()
                for child in A[node]:
                    if labels[child] == -1:
                        labels[child] = group
                        cur.append(child)
        
        for node in range(n):
            if labels[node] == -1:
                labels[node] = group
                dfs(node, group)
                group += 1
        ans = 0
        # print(labels)
        d = Counter(labels)
        for label, count in d.items():
            ans += count * (n - count)
        return ans // 2
        