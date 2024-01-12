class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        x = 0
        n = len(s)
        v = "aeiouAEIOU"
        for c in s[:n//2]:
            if c in v:
                x += 1
        for c in s[n//2:]:
            if c in v:
                x -= 1
        return x == 0