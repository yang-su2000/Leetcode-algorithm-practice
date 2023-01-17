class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        m0 = 0 if s[0] == '0' else 1
        m1 = 0 if s[0] == '1' else 1
        for c in s[1:]:
            if c == '0':
                m1 = min(m0 + 1, m1 + 1)
            else:
                m0, m1 = m0 + 1, min(m0, m1)
        return min(m0, m1)