class Solution:
    def countSubstrings(self, s: str, c: str) -> int: return s.count(c) * (s.count(c) + 1) // 2