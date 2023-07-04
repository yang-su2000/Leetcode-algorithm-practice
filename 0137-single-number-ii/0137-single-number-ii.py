class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = (1 << 32) - 1
        b = 0
        for i in nums:
            a = (a ^ i) & (~b)
            b = (b ^ i) & (~a)
            # print(i, bin(a), bin(b))
        if b >= (1 << 31):
            b = b - (1 << 32)
        return b