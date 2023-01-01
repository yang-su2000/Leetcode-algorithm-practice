class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        d2 = {}
        s2 = s.split()
        if len(pattern) != len(s2):
            return False
        for i, j in zip(pattern, s2):
            if j in d and d[j] != i:
                return False
            if i in d2 and d2[i] != j:
                return False
            d[j] = i
            d2[i] = j
        return True