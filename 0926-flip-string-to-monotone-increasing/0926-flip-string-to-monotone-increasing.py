class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        m0 = 0
        m1 = 0
        for c in s:
            if c == '0':
                m1 = min(m0, m1) + 1
            else:
                m1 = min(m0, m1)
                m0 += 1
        return min(m0, m1)