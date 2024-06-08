class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d = defaultdict(int)
        ans = 0
        for c in s:
            d[c] += 1
            ans += d[c]
        return ans