class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        g = [[] for _ in range(m)]
        for i in range(n):
            if group[i] != -1:
                g[group[i]].append(i)
            else:
                group[i] = m
                g.append([i])
                m += 1
        # print(g, group)
        Ag = [set() for _ in range(m)]
        Pg = [set() for _ in range(m)]
        A = [defaultdict(list) for i in range(m)]
        P = [defaultdict(list) for i in range(m)]
        for i in range(n):
            parents = beforeItems[i]
            for p in parents:
                if group[p] == group[i]:
                    A[group[p]][p].append(i)
                    P[group[p]][i].append(p)
                else:
                    Ag[group[p]].add(group[i])
                    Pg[group[i]].add(group[p])
        # print(Ag, Pg)
        # print(A, P)
        Countg = [len(p) for p in Ag]
        Orderg = []
        Curg = [i for i in range(m) if not len(Ag[i])]
        # print(Curg)
        while Curg:
            node = Curg.pop()
            Orderg.append(node)
            for parent in Pg[node]:
                Countg[parent] -= 1
                if Countg[parent] == 0:
                    Curg.append(parent)
        if len(Orderg) < m:
            return []
        Orderg.reverse()
        # print(Orderg)
        Orders = []
        for i in range(m):
            Asub = A[i]
            Psub = P[i]
            Count = defaultdict(int)
            Order = []
            Cur = []
            for node in g[i]:
                if node not in Asub:
                    Cur.append(node)
                else:
                    Count[node] = len(Asub[node])
            while Cur:
                node = Cur.pop()
                Order.append(node)
                if not Psub[node]:
                    continue
                for parent in Psub[node]:
                    Count[parent] -= 1
                    if Count[parent] == 0:
                        Cur.append(parent)
            if len(Order) < len(g[i]):
                return []
            Order.reverse()
            Orders.append(Order)
            # print('group', i, Cur, Count)
        ans = []
        for i in Orderg:
            ans.extend(Orders[i])
        return ans