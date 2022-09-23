class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = ''.join([str(bin(i))[2:] for i in range(1, n+1)])
        modulo = str(bin(10**9+7))[2:]
        return int(ans, 2) % int(modulo, 2)