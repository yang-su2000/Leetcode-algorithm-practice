class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        A = defaultdict(list)
        for a, b in adjacentPairs:
            A[a].append(b)
            A[b].append(a)
        ans = []
        vis = set()
        for node in A.keys():
            if node in vis:
                continue
            vis.add(node)
            ls = [[], []]
            for i, a in enumerate(A[node]):
                b = node
                while True:
                    vis.add(a)
                    ls[i].append(a)
                    if len(A[a]) <= 1: break
                    a, b = A[a][0] if A[a][0] != b else A[a][1], a
            # print(ls[0][::-1], node, ls[1])
            ans.extend(ls[0][::-1] + [node] + ls[1])
        return ans