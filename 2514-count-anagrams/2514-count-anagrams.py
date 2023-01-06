class Solution:
    def countAnagrams(self, s: str) -> int:
        ans = 1
        cur = 1
        idx = 1
        mod = 1000000007
        d = defaultdict(int)
        for c in s:
            if c == ' ':
                ans = ans * cur % mod
                cur = 1
                idx = 1
                d = defaultdict(int)
            else:
                d[c] += 1
                cur = cur * idx // d[c]
                idx += 1
        return ans * cur % mod