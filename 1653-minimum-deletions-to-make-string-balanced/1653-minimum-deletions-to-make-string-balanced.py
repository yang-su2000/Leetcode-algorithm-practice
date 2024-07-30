class Solution:
    def minimumDeletions(self, s: str) -> int:
        a, b = 0, 0
        for c in s:
            if c == 'a':
                b = min(a, b + 1)
            else:
                a += 1
        return min(a, b)