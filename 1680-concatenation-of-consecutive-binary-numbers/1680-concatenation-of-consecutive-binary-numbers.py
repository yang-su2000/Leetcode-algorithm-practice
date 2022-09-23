class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = 0
        cur = 1
        l = 0
        modulo = 10**9+7
        for i in range(1, n+1):
            if i == cur:
                l += 1
                cur *= 2
            ans <<= l
            ans = (ans + i) % modulo
        return ans