class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        d = defaultdict(int)
        d['$'] = 0
        for c in s:
            d2 = d.copy()
            for c2, val in d.items():
                if c2 == '$' or abs(ord(c2) - ord(c)) <= k:
                    d2[c] = max(d2[c], val + 1)
            d = d2
        return max(d.values())