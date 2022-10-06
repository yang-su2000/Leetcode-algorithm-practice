class Solution:
    def reverseBits(self, n: int) -> int:
        s = str(bin(n))[2:]
        s = '0' * (32 - len(s)) + s
        # print(s)
        return int(s[::-1], 2)