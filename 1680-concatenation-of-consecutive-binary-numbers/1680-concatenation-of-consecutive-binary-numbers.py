class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = 0
        modulo = 10**9+7
        for i in range(1, n+1):
            ans <<= len(str(bin(i))) - 2
            ans = (ans + i) % modulo
        return ans