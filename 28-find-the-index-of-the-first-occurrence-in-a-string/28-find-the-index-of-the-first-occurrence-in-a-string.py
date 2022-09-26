class Solution:
    def strStr(self, N: str, M: str) -> int:
        n = len(N)
        m = len(M)
        for i in range(n - m + 1):
            if N[i:i+m] == M:
                return i
        return -1