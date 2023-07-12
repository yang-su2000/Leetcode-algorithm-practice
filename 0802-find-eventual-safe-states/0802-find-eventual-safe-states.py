class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        count = [0] * n
        parents = [[] for _ in range(n)]
        cur = []
        for node, children in enumerate(graph):
            count[node] = len(children)
            for child in children:
                parents[child].append(node)
            if not children:
                cur.append(node)
        ans = cur.copy()
        while cur:
            node = cur.pop()
            for parent in parents[node]:
                count[parent] -= 1
                if count[parent] == 0:
                    cur.append(parent)
                    ans.append(parent)
        return sorted(ans)