class Solution:
    def minCost(self, colors: str, t: List[int]) -> int:
        q = [t[0]]
        c = colors[0]
        ans = 0
        for i in range(1, len(t)):
            if colors[i] == c:
                q.append(t[i])
            else:
                if len(q) > 1:
                    ans += sum(q) - max(q)
                q = [t[i]]
                c = colors[i]
        if len(q) > 1:
            ans += sum(q) - max(q)
        return ans