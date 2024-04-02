class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        for c1, c2 in zip(s, t):
            if c1 in d1:
                if d1[c1] != c2:
                    return False
            elif c2 in d2:
                if d2[c2] != c1:
                    return False
            else:
                d1[c1] = c2
                d2[c2] = c1
        return True