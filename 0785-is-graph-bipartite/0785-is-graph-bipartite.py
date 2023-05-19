class Solution:
    def isBipartite(self, A: List[List[int]]) -> bool:
        n = len(A)
        color = [-1] * n
        for node in range(n):
            if not A[node]:
                continue
            if color[node] != -1:
                continue
            color[node] = 0
            cur = [node]
            while cur:
                node = cur.pop()
                c = 0 if color[node] else 1
                for child in A[node]:
                    if color[child] == -1:
                        color[child] = c
                        cur.append(child)
                    elif color[child] != c:
                        return False
        # print(color)
        return True