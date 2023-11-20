class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        n = len(garbage)
        ans = [0] * 3
        for idx, t in enumerate('MPG'):
            cur = garbage[0].count(t)
            ans[idx] = cur
            for i in range(1, n):
                cur += travel[i-1]
                if t in garbage[i]:
                    cur += garbage[i].count(t)
                    ans[idx] = cur
        return sum(ans)