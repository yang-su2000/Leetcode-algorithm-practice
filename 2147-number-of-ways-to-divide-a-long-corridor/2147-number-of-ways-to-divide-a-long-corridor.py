class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = int(1e9+7)
        ans = 1
        s = 0
        p = 1
        for c in corridor:
            if s < 2:
                if c == 'S':
                    s += 1
            elif c == 'P':
                p += 1
            else:
                ans = (ans * p) % mod
                s = 1
                p = 1
        return ans if s == 2 else 0