import heapq

class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], src: int, dst: int, target: int) -> List[List[int]]:
        A = [[] for _ in range(n)]
        for a, b, w in edges:
            A[a].append((b, w))
            A[b].append((a, w))
        
        def dij(start, use_neg):
            nonlocal A
            d = defaultdict(lambda: inf)
            d[start] = 0
            parent = {}
            cur = [(0, start)]
            while cur:
                w, node = heappop(cur)
                if w > d[node]:
                    continue
                for child, w2 in A[node]:
                    if w2 == -1:
                        if use_neg:
                            w2 = 1
                        else:
                            continue
                    if w + w2 < d[child]:
                        d[child] = w + w2
                        parent[child] = node
                        heappush(cur, (w + w2, child))
            return d, parent
        
        d1, parent1 = dij(start=dst, use_neg=False) # dst -> src w/o neg
        if d1[src] < target:
            return []
        
        d2, parent2 = dij(start=src, use_neg=True) # src -> dst w/ neg = 1
        if d2[dst] > target:
            return []
        
        # print(d1.items(), parent1.items())
        # print(d2.items(), parent2.items())
        
        path = [dst]
        while path[-1] != src:
            path.append(parent2[path[-1]])
        path = path[::-1] # a modified path from src -> dst by taking neg = 1
        
        # print(path)
        
        d_edge = {(min(u, v), max(u, v)): w for u, v, w in edges}
        w_total = 0
        for i in range(len(path) - 1):
            u, v = path[i], path[i+1]
            e = (min(u, v), max(u, v))
            
            # most important step
            # w of (u, v) is modified to 
            # target - w of (src, u) [modified] - w of (v, dst) [unmodified]
            if d_edge[e] == -1:
                d_edge[e] = max(target - w_total - d1[v], 1)
            w_total += d_edge[e]
        
        # print(d_change.items())
        
        ans = []
        for u, v, w in edges:
            if w == -1:
                e = (min(u, v), max(u, v))
                if d_edge[e] == -1:
                    w = int(2e9)
                else:
                    w = d_edge[e]
            ans.append([u, v, w])
        return ans