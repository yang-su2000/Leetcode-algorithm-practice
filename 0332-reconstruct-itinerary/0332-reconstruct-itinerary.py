class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        n = len(tickets)
        d = defaultdict(lambda: defaultdict(int))
        for a, b in tickets:
            d[a][b] += 1
        # print(d)
        ans = None
        
        def bt(cur):
            nonlocal n, d, ans
            if len(cur) == n + 1:
                ans = cur.copy()
                return
            node = cur[-1]
            for child in sorted(d[node].keys()):
                if not d[node][child]:
                    continue
                if ans and ans[len(cur)] <= child:
                    continue
                d[node][child] -= 1
                cur.append(child)
                bt(cur)
                cur.pop()
                d[node][child] += 1
        
        bt(["JFK"])
        return ans